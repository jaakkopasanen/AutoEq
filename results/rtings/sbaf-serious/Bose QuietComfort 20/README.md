# Bose QuietComfort 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 -1.7; 23 -3.6; 25 -5.2; 28 -6.8; 31 -7.8; 34 -8.4; 37 -8.7; 41 -8.8; 45 -8.8; 49 -8.8; 54 -8.7; 60 -8.6; 66 -8.6; 72 -8.5; 79 -8.6; 87 -8.7; 96 -8.9; 106 -9.0; 116 -9.0; 128 -8.8; 141 -8.3; 155 -7.9; 170 -7.7; 187 -7.6; 206 -7.6; 227 -7.6; 249 -7.4; 274 -7.1; 302 -7.0; 332 -6.8; 365 -6.5; 402 -6.0; 442 -5.3; 486 -4.3; 535 -3.2; 588 -2.0; 647 -0.8; 712 0.3; 783 1.3; 861 1.7; 947 0.7; 1042 -0.4; 1146 -1.3; 1261 -2.3; 1387 -3.6; 1526 -5.2; 1678 -6.9; 1846 -7.6; 2031 -7.4; 2234 -6.3; 2457 -4.8; 2703 -3.8; 2973 -3.3; 3270 -3.1; 3597 -4.4; 3957 -7.6; 4353 -9.1; 4788 -5.3; 5267 -0.4; 5793 1.1; 6373 -3.3; 7010 -2.3; 7711 0.2; 8482 -0.1; 9330 -1.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.84 | -7.1 dB |
| Peaking | 123 Hz  | 0.65 | -7.4 dB |
| Peaking | 327 Hz  | 1.5  | -4.8 dB |
| Peaking | 1930 Hz | 2.12 | -8.0 dB |
| Peaking | 4224 Hz | 4.11 | -9.1 dB |
| Peaking | 471 Hz  | 3.63 | -1.5 dB |
| Peaking | 832 Hz  | 2.65 | 3.3 dB  |
| Peaking | 1506 Hz | 4.07 | -1.3 dB |
| Peaking | 5649 Hz | 7.66 | 3.5 dB  |
| Peaking | 6618 Hz | 9.61 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)