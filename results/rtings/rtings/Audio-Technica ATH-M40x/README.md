# Audio-Technica ATH-M40x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 0.0; 23 0.7; 25 0.1; 28 -0.7; 31 -1.3; 34 -1.8; 37 -2.2; 41 -2.6; 45 -2.9; 49 -3.1; 54 -3.2; 60 -3.3; 66 -3.4; 72 -3.3; 79 -3.0; 87 -3.2; 96 -4.0; 106 -4.9; 116 -5.6; 128 -5.7; 141 -5.3; 155 -5.0; 170 -4.8; 187 -4.1; 206 -3.1; 227 -1.9; 249 -0.8; 274 0.2; 302 1.1; 332 1.9; 365 1.8; 402 1.2; 442 1.2; 486 1.1; 535 0.8; 588 0.6; 647 0.6; 712 0.6; 783 0.6; 861 0.7; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.5; 1387 -1.7; 1526 -1.9; 1678 -2.2; 1846 -2.2; 2031 -2.1; 2234 -1.3; 2457 -0.2; 2703 0.4; 2973 0.2; 3270 -0.4; 3597 -0.2; 3957 -0.1; 4353 -1.2; 4788 0.8; 5267 3.0; 5793 4.2; 6373 2.3; 7010 -0.1; 7711 -2.3; 8482 -4.9; 9330 -7.6; 10263 -7.5; 11289 -3.3; 12418 0.0; 13660 -2.0; 15026 -6.8; 16529 -5.7; 18182 -0.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 1.11 | -2.9 dB |
| Peaking | 135 Hz   | 1.62 | -5.7 dB |
| Peaking | 5837 Hz  | 4.46 | 5.3 dB  |
| Peaking | 9559 Hz  | 3.04 | -8.6 dB |
| Peaking | 15731 Hz | 3.1  | -7.7 dB |
| Peaking | 199 Hz   | 3.13 | -1.9 dB |
| Peaking | 347 Hz   | 1.45 | 2.4 dB  |
| Peaking | 835 Hz   | 2.66 | 0.9 dB  |
| Peaking | 1621 Hz  | 1.65 | -2.4 dB |
| Peaking | 12470 Hz | 7.41 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-M40x/Audio-Technica%20ATH-M40x.png)