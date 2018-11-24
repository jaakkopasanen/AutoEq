# Oppo PM1 2014 PM2 Pad

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.8; 28 1.6; 31 1.5; 34 1.4; 37 1.3; 41 1.2; 45 1.2; 49 1.3; 54 1.5; 60 1.5; 66 1.0; 72 0.3; 79 -0.2; 87 -0.8; 96 -1.2; 106 -1.5; 116 -1.7; 128 -2.0; 141 -2.3; 155 -2.3; 170 -2.4; 187 -2.6; 206 -2.6; 227 -2.3; 249 -2.7; 274 -3.1; 302 -3.3; 332 -3.2; 365 -1.4; 402 0.1; 442 -0.4; 486 -1.2; 535 -1.6; 588 -1.5; 647 -1.8; 712 -2.1; 783 -2.1; 861 -2.3; 947 -0.5; 1042 -0.1; 1146 -0.7; 1261 -1.0; 1387 -1.6; 1526 -2.1; 1678 -2.4; 1846 -2.2; 2031 -1.9; 2234 -1.5; 2457 -0.6; 2703 0.5; 2973 1.7; 3270 2.1; 3597 1.9; 3957 2.4; 4353 2.6; 4788 3.7; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.7; 9330 -1.9; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 2014 PM2 Pad GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 2014 PM2 Pad ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 80 Hz   | 0.16 | 2.7 dB  |
| Peaking | 163 Hz  | 0.56 | -3.3 dB |
| Peaking | 302 Hz  | 0.3  | -2.1 dB |
| Peaking | 1762 Hz | 2.87 | -2.4 dB |
| Peaking | 5501 Hz | 2.26 | 6.5 dB  |
| Peaking | 320 Hz  | 4.16 | -1.7 dB |
| Peaking | 402 Hz  | 4.68 | 2.4 dB  |
| Peaking | 762 Hz  | 4.57 | -1.2 dB |
| Peaking | 3211 Hz | 4.48 | 1.8 dB  |
| Peaking | 8974 Hz | 5.09 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%202014%20PM2%20Pad/Oppo%20PM1%202014%20PM2%20Pad.png)