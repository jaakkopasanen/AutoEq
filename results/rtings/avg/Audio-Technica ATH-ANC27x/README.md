# Audio-Technica ATH-ANC27x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -15.5; 23 -15.7; 25 -15.7; 28 -15.2; 31 -14.4; 34 -13.4; 37 -12.4; 41 -11.9; 45 -11.8; 49 -11.3; 54 -10.6; 60 -9.9; 66 -9.5; 72 -9.0; 79 -8.7; 87 -8.3; 96 -8.0; 106 -8.0; 116 -8.0; 128 -7.8; 141 -7.5; 155 -7.3; 170 -6.9; 187 -6.5; 206 -6.1; 227 -5.8; 249 -5.4; 274 -5.1; 302 -4.7; 332 -4.2; 365 -3.7; 402 -3.3; 442 -2.8; 486 -2.4; 535 -2.0; 588 -1.4; 647 -0.6; 712 0.6; 783 1.1; 861 0.6; 947 0.5; 1042 -0.4; 1146 -0.3; 1261 0.1; 1387 1.8; 1526 4.4; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 4.9; 2973 3.0; 3270 5.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.9; 5267 3.8; 5793 -1.1; 6373 -7.6; 7010 -5.2; 7711 -3.7; 8482 -0.5; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -2.3; 13660 -0.1; 15026 0.0; 16529 -0.2; 18182 -1.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC27x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC27x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.37 | -15.4 dB |
| Peaking | 180 Hz   | 0.52 | -4.9 dB  |
| Peaking | 1959 Hz  | 1.73 | 5.9 dB   |
| Peaking | 4737 Hz  | 1.25 | 8.3 dB   |
| Peaking | 6508 Hz  | 2.74 | -12.3 dB |
| Peaking | 780 Hz   | 3.81 | 2.1 dB   |
| Peaking | 1247 Hz  | 2.09 | -1.9 dB  |
| Peaking | 1570 Hz  | 5.86 | 2.3 dB   |
| Peaking | 12487 Hz | 9.05 | -2.7 dB  |
| Peaking | 17662 Hz | 4.01 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC27x/Audio-Technica%20ATH-ANC27x.png)