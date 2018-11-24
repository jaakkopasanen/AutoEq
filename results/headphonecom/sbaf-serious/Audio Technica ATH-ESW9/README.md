# Audio Technica ATH-ESW9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 5.8; 72 6.0; 79 5.5; 87 5.0; 96 4.8; 106 4.6; 116 4.6; 128 5.4; 141 4.9; 155 4.6; 170 4.6; 187 4.7; 206 4.6; 227 4.2; 249 3.9; 274 3.4; 302 3.2; 332 3.8; 365 4.1; 402 4.5; 442 4.6; 486 4.7; 535 4.6; 588 4.5; 647 3.6; 712 2.2; 783 1.3; 861 0.8; 947 0.2; 1042 -0.3; 1146 -0.9; 1261 -1.2; 1387 -1.7; 1526 -2.3; 1678 -2.3; 1846 -1.6; 2031 -0.7; 2234 0.6; 2457 2.1; 2703 4.1; 2973 5.8; 3270 6.0; 3597 6.0; 3957 5.6; 4353 4.3; 4788 5.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ESW9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ESW9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.25 | 6.1 dB  |
| Peaking | 204 Hz  | 0.92 | 2.4 dB  |
| Peaking | 499 Hz  | 1.99 | 4.3 dB  |
| Peaking | 3333 Hz | 2.87 | 6.2 dB  |
| Peaking | 5486 Hz | 2.53 | 6.1 dB  |
| Peaking | 640 Hz  | 6.1  | 1.3 dB  |
| Peaking | 1193 Hz | 2.79 | -0.9 dB |
| Peaking | 1659 Hz | 2.34 | -3.0 dB |
| Peaking | 2755 Hz | 5.51 | 1.9 dB  |
| Peaking | 8283 Hz | 4.59 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ESW9/Audio%20Technica%20ATH-ESW9.png)