# Audiofly Adagio Club Life

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.6; 34 5.2; 37 4.8; 41 4.3; 45 3.9; 49 3.5; 54 3.1; 60 2.6; 66 2.2; 72 1.8; 79 1.2; 87 0.9; 96 0.4; 106 0.1; 116 -0.1; 128 -0.5; 141 -0.7; 155 -0.9; 170 -1.2; 187 -1.2; 206 -1.3; 227 -1.1; 249 -1.2; 274 -1.0; 302 -0.8; 332 -0.7; 365 -0.4; 402 -0.1; 442 0.3; 486 0.5; 535 0.8; 588 1.2; 647 1.4; 712 1.2; 783 1.3; 861 1.0; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -1.8; 1387 -2.4; 1526 -2.4; 1678 -1.9; 1846 -0.8; 2031 0.5; 2234 1.4; 2457 2.1; 2703 2.1; 2973 1.4; 3270 1.9; 3597 4.2; 3957 6.0; 4353 5.7; 4788 5.2; 5267 5.0; 5793 3.3; 6373 1.5; 7010 -0.7; 7711 -0.9; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audiofly Adagio Club Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audiofly Adagio Club Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.22 | 6.2 dB  |
| Peaking | 49 Hz   | 1.81 | 2.4 dB  |
| Peaking | 1489 Hz | 3.11 | -3.1 dB |
| Peaking | 2414 Hz | 4.39 | 1.7 dB  |
| Peaking | 4369 Hz | 2.12 | 6.4 dB  |
| Peaking | 215 Hz  | 1.06 | -1.5 dB |
| Peaking | 700 Hz  | 1.4  | 1.7 dB  |
| Peaking | 1178 Hz | 3.63 | -1.0 dB |
| Peaking | 5521 Hz | 6.63 | 1.7 dB  |
| Peaking | 7293 Hz | 4.69 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audiofly%20Adagio%20Club%20Life/Audiofly%20Adagio%20Club%20Life.png)