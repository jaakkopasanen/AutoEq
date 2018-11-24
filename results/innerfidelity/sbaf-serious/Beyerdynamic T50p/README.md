# Beyerdynamic T50p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.6; 45 5.1; 49 4.6; 54 4.0; 60 3.3; 66 2.8; 72 2.4; 79 2.1; 87 1.9; 96 1.4; 106 2.2; 116 2.5; 128 2.4; 141 2.5; 155 3.0; 170 3.0; 187 1.3; 206 -0.6; 227 -1.7; 249 -2.4; 274 -2.4; 302 -2.8; 332 -3.3; 365 -3.2; 402 -2.9; 442 -2.7; 486 -2.6; 535 -2.3; 588 -1.7; 647 -1.5; 712 -0.7; 783 -0.0; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.9; 1387 0.9; 1526 1.0; 1678 1.3; 1846 2.3; 2031 3.9; 2234 5.9; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.56 | 6.4 dB  |
| Peaking | 159 Hz  | 1.7  | 4.7 dB  |
| Peaking | 295 Hz  | 0.67 | -4.1 dB |
| Peaking | 2859 Hz | 1.16 | 6.2 dB  |
| Peaking | 5385 Hz | 2.21 | 5.0 dB  |
| Peaking | 1687 Hz | 4.61 | -1.0 dB |
| Peaking | 2225 Hz | 7.84 | 1.5 dB  |
| Peaking | 6320 Hz | 6.79 | 1.5 dB  |
| Peaking | 6643 Hz | 6.08 | 1.5 dB  |
| Peaking | 7701 Hz | 2    | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)