# Audio-Technica ATH-ANC7B SVIS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.3; 28 3.5; 31 2.9; 34 2.3; 37 1.9; 41 1.5; 45 1.1; 49 0.7; 54 0.2; 60 -0.3; 66 -0.5; 72 -0.7; 79 -0.9; 87 -1.0; 96 -1.4; 106 -2.0; 116 -2.6; 128 -2.8; 141 -2.9; 155 -2.9; 170 -2.7; 187 -2.3; 206 -2.0; 227 -1.7; 249 -1.5; 274 -1.3; 302 -1.1; 332 -0.9; 365 -0.8; 402 -0.9; 442 -1.0; 486 -1.4; 535 -1.8; 588 -2.4; 647 -1.4; 712 1.2; 783 2.2; 861 1.0; 947 -0.5; 1042 1.8; 1146 5.4; 1261 6.0; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.9; 5793 4.6; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.1; 13660 -3.6; 15026 -4.6; 16529 -5.8; 18182 -4.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7B SVIS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7B SVIS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.94 | 5.9 dB  |
| Peaking | 146 Hz   | 0.88 | -3.1 dB |
| Peaking | 592 Hz   | 1.34 | -3.6 dB |
| Peaking | 2501 Hz  | 0.37 | 6.8 dB  |
| Peaking | 16148 Hz | 1.08 | -6.3 dB |
| Peaking | 782 Hz   | 3.93 | 4.3 dB  |
| Peaking | 987 Hz   | 2.01 | -6.5 dB |
| Peaking | 1166 Hz  | 2.94 | 5.7 dB  |
| Peaking | 6625 Hz  | 2.17 | 3.6 dB  |
| Peaking | 7632 Hz  | 2.76 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-ANC7B%20SVIS/Audio-Technica%20ATH-ANC7B%20SVIS.png)