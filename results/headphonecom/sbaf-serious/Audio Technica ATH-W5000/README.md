# Audio Technica ATH-W5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 5.9; 274 5.6; 302 5.5; 332 5.7; 365 5.8; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 5.4; 647 3.2; 712 1.7; 783 1.3; 861 0.8; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.5; 1387 -2.3; 1526 -2.8; 1678 -2.1; 1846 -1.9; 2031 -1.8; 2234 -0.1; 2457 2.1; 2703 5.2; 2973 6.0; 3270 6.0; 3597 5.7; 3957 0.6; 4353 2.3; 4788 5.7; 5267 6.0; 5793 6.0; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.7; 10263 -1.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.7; 16529 -5.1; 18182 -7.6; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-W5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 0.07 | 6.3 dB  |
| Peaking | 1523 Hz  | 0.78 | -6.7 dB |
| Peaking | 2986 Hz  | 2.53 | 7.8 dB  |
| Peaking | 5504 Hz  | 2.95 | 6.6 dB  |
| Peaking | 19032 Hz | 1.14 | -8.9 dB |
| Peaking | 565 Hz   | 2.39 | 3.0 dB  |
| Peaking | 691 Hz   | 2.54 | -2.6 dB |
| Peaking | 6798 Hz  | 7.69 | 1.0 dB  |
| Peaking | 9516 Hz  | 7.4  | -4.3 dB |
| Peaking | 13373 Hz | 2.7  | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-W5000/Audio%20Technica%20ATH-W5000.png)