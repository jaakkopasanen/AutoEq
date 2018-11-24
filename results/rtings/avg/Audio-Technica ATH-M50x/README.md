# Audio-Technica ATH-M50x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 0.1; 25 -0.2; 28 -0.6; 31 -0.9; 34 -1.1; 37 -1.2; 41 -1.3; 45 -1.2; 49 -1.0; 54 -0.7; 60 -0.4; 66 -0.2; 72 -0.2; 79 -0.6; 87 -1.3; 96 -2.0; 106 -2.4; 116 -2.6; 128 -2.6; 141 -2.6; 155 -2.7; 170 -2.4; 187 -1.9; 206 -1.0; 227 0.2; 249 1.6; 274 3.0; 302 3.5; 332 3.2; 365 3.1; 402 2.1; 442 1.1; 486 0.5; 535 0.1; 588 -0.0; 647 -0.2; 712 -0.1; 783 -0.1; 861 -0.1; 947 -0.0; 1042 0.1; 1146 0.2; 1261 0.1; 1387 -0.1; 1526 -0.1; 1678 -0.8; 1846 -2.3; 2031 -3.0; 2234 -2.1; 2457 -1.3; 2703 -0.6; 2973 -0.4; 3270 0.6; 3597 1.1; 3957 -1.4; 4353 -3.8; 4788 -0.7; 5267 3.4; 5793 5.9; 6373 4.1; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.8; 11289 -2.7; 12418 -1.7; 13660 0.0; 15026 0.0; 16529 -1.7; 18182 -5.8; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 156 Hz   | 0.88 | -3.5 dB |
| Peaking | 302 Hz   | 1.68 | 5.1 dB  |
| Peaking | 4521 Hz  | 0.42 | -1.8 dB |
| Peaking | 5979 Hz  | 3.4  | 7.9 dB  |
| Peaking | 18743 Hz | 2.01 | -6.5 dB |
| Peaking | 2038 Hz  | 5.25 | -2.5 dB |
| Peaking | 3825 Hz  | 2.05 | 3.8 dB  |
| Peaking | 4291 Hz  | 5.05 | -6.6 dB |
| Peaking | 11687 Hz | 3.67 | -4.4 dB |
| Peaking | 12415 Hz | 1.35 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M50x/Audio-Technica%20ATH-M50x.png)