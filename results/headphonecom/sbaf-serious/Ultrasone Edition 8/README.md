# Ultrasone Edition 8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 5.1; 45 4.5; 49 3.6; 54 2.3; 60 1.1; 66 1.6; 72 0.9; 79 -0.3; 87 -1.2; 96 -2.0; 106 -2.8; 116 -3.4; 128 -3.9; 141 -4.3; 155 -3.5; 170 -4.0; 187 -3.8; 206 -3.8; 227 -3.1; 249 -4.0; 274 -2.9; 302 -2.4; 332 -1.8; 365 -0.8; 402 -0.2; 442 0.2; 486 0.7; 535 1.0; 588 1.0; 647 -0.3; 712 -0.0; 783 0.2; 861 -0.1; 947 -0.1; 1042 -0.2; 1146 -0.4; 1261 -0.5; 1387 -0.6; 1526 -0.6; 1678 -0.2; 1846 0.3; 2031 3.6; 2234 5.7; 2457 2.9; 2703 -1.3; 2973 0.2; 3270 1.1; 3597 -0.8; 3957 -5.2; 4353 -2.5; 4788 -0.8; 5267 2.9; 5793 2.2; 6373 -4.3; 7010 -4.3; 7711 -1.8; 8482 -0.0; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.3; 15026 -1.2; 16529 -0.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.66 | 6.7 dB  |
| Peaking | 148 Hz  | 0.82 | -5.0 dB |
| Peaking | 2039 Hz | 1.83 | -1.9 dB |
| Peaking | 2189 Hz | 5.05 | 8.3 dB  |
| Peaking | 4010 Hz | 8.07 | -5.5 dB |
| Peaking | 256 Hz  | 5.48 | -1.5 dB |
| Peaking | 515 Hz  | 2.7  | 1.7 dB  |
| Peaking | 5574 Hz | 7.24 | 8.6 dB  |
| Peaking | 6537 Hz | 2.87 | -6.4 dB |
| Peaking | 8505 Hz | 3.8  | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Edition%208/Ultrasone%20Edition%208.png)