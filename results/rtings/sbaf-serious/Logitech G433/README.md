# Logitech G433

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.6; 28 -0.0; 31 -0.6; 34 -1.1; 37 -1.5; 41 -2.0; 45 -2.1; 49 -2.2; 54 -2.3; 60 -2.2; 66 -2.2; 72 -2.0; 79 -1.9; 87 -2.0; 96 -2.4; 106 -3.1; 116 -3.8; 128 -4.2; 141 -4.2; 155 -4.2; 170 -4.1; 187 -3.8; 206 -3.2; 227 -2.6; 249 -1.9; 274 -0.9; 302 -0.0; 332 0.8; 365 1.4; 402 1.4; 442 0.9; 486 0.1; 535 -1.0; 588 -2.0; 647 -2.7; 712 -2.8; 783 -2.3; 861 -1.3; 947 -0.3; 1042 0.2; 1146 0.2; 1261 0.0; 1387 -0.4; 1526 -0.4; 1678 -0.2; 1846 -0.3; 2031 -0.8; 2234 -0.6; 2457 0.4; 2703 1.2; 2973 2.1; 3270 3.0; 3597 1.5; 3957 -3.0; 4353 -3.6; 4788 -0.9; 5267 1.6; 5793 5.6; 6373 5.5; 7010 2.5; 7711 -0.3; 8482 -3.3; 9330 -3.8; 10263 -0.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G433 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G433 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 136 Hz  | 1.06 | -4.5 dB |
| Peaking | 703 Hz  | 3.8  | -3.2 dB |
| Peaking | 4406 Hz | 3.65 | -8.7 dB |
| Peaking | 6251 Hz | 1.01 | 8.7 dB  |
| Peaking | 8589 Hz | 2.1  | -8.9 dB |
| Peaking | 18 Hz   | 1.49 | 2.4 dB  |
| Peaking | 46 Hz   | 1.74 | -2.0 dB |
| Peaking | 378 Hz  | 3.5  | 2.5 dB  |
| Peaking | 2711 Hz | 1    | -1.6 dB |
| Peaking | 3187 Hz | 3.66 | 3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Logitech%20G433/Logitech%20G433.png)