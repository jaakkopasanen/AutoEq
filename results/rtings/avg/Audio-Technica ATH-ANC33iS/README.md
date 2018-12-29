# Audio-Technica ATH-ANC33iS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.3; 37 4.8; 41 4.2; 45 3.6; 49 3.0; 54 2.3; 60 1.4; 66 0.6; 72 -0.1; 79 -0.9; 87 -1.8; 96 -2.7; 106 -3.7; 116 -4.7; 128 -5.6; 141 -6.5; 155 -7.2; 170 -7.8; 187 -8.3; 206 -8.6; 227 -8.8; 249 -8.9; 274 -9.0; 302 -9.2; 332 -9.2; 365 -9.1; 402 -8.9; 442 -8.4; 486 -7.9; 535 -7.0; 588 -6.0; 647 -4.4; 712 -3.1; 783 -1.3; 861 -0.7; 947 -0.4; 1042 0.4; 1146 1.0; 1261 -0.1; 1387 -3.0; 1526 -5.5; 1678 -5.7; 1846 -4.4; 2031 -2.6; 2234 -0.3; 2457 1.5; 2703 2.0; 2973 1.0; 3270 -0.8; 3597 -2.5; 3957 -3.6; 4353 -4.7; 4788 -5.6; 5267 -7.1; 5793 -6.2; 6373 -5.2; 7010 -2.6; 7711 -1.2; 8482 -2.3; 9330 -3.2; 10263 -0.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC33iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC33iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.67 | 6.7 dB   |
| Peaking | 256 Hz   | 0.58 | -10.1 dB |
| Peaking | 1657 Hz  | 5.64 | -5.6 dB  |
| Peaking | 5407 Hz  | 2.14 | -7.3 dB  |
| Peaking | 20139 Hz | 3.91 | -3.7 dB  |
| Peaking | 508 Hz   | 2.35 | -2.5 dB  |
| Peaking | 1152 Hz  | 1.32 | 6.4 dB   |
| Peaking | 1447 Hz  | 1.28 | -5.2 dB  |
| Peaking | 2681 Hz  | 3.2  | 4.0 dB   |
| Peaking | 3883 Hz  | 3.56 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC33iS/Audio-Technica%20ATH-ANC33iS.png)