# Audio-Technica ATH-M50x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.1; 25 -0.2; 28 -0.6; 31 -0.9; 34 -1.1; 37 -1.2; 41 -1.3; 45 -1.2; 49 -1.0; 54 -0.7; 60 -0.4; 66 -0.2; 72 -0.2; 79 -0.6; 87 -1.3; 96 -2.0; 106 -2.4; 116 -2.6; 128 -2.6; 141 -2.6; 155 -2.7; 170 -2.4; 187 -1.9; 206 -1.0; 227 0.2; 249 1.6; 274 3.0; 302 3.5; 332 3.2; 365 3.1; 402 2.1; 442 1.1; 486 0.5; 535 0.1; 588 -0.0; 647 -0.2; 712 -0.1; 783 -0.1; 861 -0.1; 947 -0.0; 1042 0.1; 1146 0.2; 1261 0.1; 1387 -0.1; 1526 -0.1; 1678 -0.8; 1846 -2.3; 2031 -3.0; 2234 -2.1; 2457 -1.2; 2703 -0.4; 2973 0.1; 3270 1.3; 3597 2.2; 3957 -0.2; 4353 -2.5; 4788 1.1; 5267 5.7; 5793 6.0; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.5; 10263 -3.0; 11289 -1.9; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 159 Hz   | 0.83 | -3.5 dB |
| Peaking | 300 Hz   | 1.72 | 5.3 dB  |
| Peaking | 2037 Hz  | 3.94 | -3.3 dB |
| Peaking | 5888 Hz  | 3.63 | 7.0 dB  |
| Peaking | 10287 Hz | 3.91 | -3.5 dB |
| Peaking | 37 Hz    | 1.79 | -1.0 dB |
| Peaking | 69 Hz    | 3.7  | 1.2 dB  |
| Peaking | 4105 Hz  | 2.32 | 3.6 dB  |
| Peaking | 4322 Hz  | 5.87 | -7.5 dB |
| Peaking | 18172 Hz | 4.36 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-M50x/Audio-Technica%20ATH-M50x.png)