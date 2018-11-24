# Audio-Technica ATH-M40x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.4; 28 -0.5; 31 -1.3; 34 -1.9; 37 -2.3; 41 -2.8; 45 -3.2; 49 -3.4; 54 -3.5; 60 -3.6; 66 -3.5; 72 -3.3; 79 -2.9; 87 -2.9; 96 -3.5; 106 -4.4; 116 -5.1; 128 -5.2; 141 -4.8; 155 -4.4; 170 -4.2; 187 -3.6; 206 -2.6; 227 -1.4; 249 -0.2; 274 0.9; 302 1.9; 332 2.8; 365 2.8; 402 2.3; 442 2.4; 486 2.3; 535 2.0; 588 1.7; 647 1.6; 712 1.5; 783 1.1; 861 0.8; 947 0.5; 1042 -0.3; 1146 -0.8; 1261 -1.3; 1387 -1.7; 1526 -2.3; 1678 -2.5; 1846 -2.1; 2031 -1.7; 2234 -0.8; 2457 0.3; 2703 1.0; 2973 1.2; 3270 1.4; 3597 2.0; 3957 1.1; 4353 -1.1; 4788 0.6; 5267 3.4; 5793 5.6; 6373 4.9; 7010 2.5; 7711 -1.1; 8482 -4.5; 9330 -6.1; 10263 -4.1; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 -3.5; 16529 -2.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 1.64 | -2.8 dB |
| Peaking | 145 Hz   | 0.89 | -5.5 dB |
| Peaking | 355 Hz   | 1.15 | 4.2 dB  |
| Peaking | 6101 Hz  | 3.3  | 6.8 dB  |
| Peaking | 9145 Hz  | 3.11 | -7.1 dB |
| Peaking | 1692 Hz  | 2.05 | -3.1 dB |
| Peaking | 3534 Hz  | 1.52 | 2.2 dB  |
| Peaking | 4405 Hz  | 6.4  | -3.6 dB |
| Peaking | 12339 Hz | 3.11 | 1.4 dB  |
| Peaking | 15540 Hz | 3.86 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-M40x/Audio-Technica%20ATH-M40x.png)