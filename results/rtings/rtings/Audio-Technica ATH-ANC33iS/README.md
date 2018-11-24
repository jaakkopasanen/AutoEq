# Audio-Technica ATH-ANC33iS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.3; 37 4.8; 41 4.2; 45 3.6; 49 3.0; 54 2.3; 60 1.4; 66 0.6; 72 -0.1; 79 -0.9; 87 -1.8; 96 -2.7; 106 -3.7; 116 -4.7; 128 -5.6; 141 -6.5; 155 -7.2; 170 -7.8; 187 -8.3; 206 -8.6; 227 -8.8; 249 -8.9; 274 -9.0; 302 -9.2; 332 -9.2; 365 -9.1; 402 -8.9; 442 -8.4; 486 -7.9; 535 -7.0; 588 -6.0; 647 -4.4; 712 -3.1; 783 -1.3; 861 -0.7; 947 -0.4; 1042 0.4; 1146 1.0; 1261 -0.1; 1387 -3.0; 1526 -5.5; 1678 -5.7; 1846 -4.4; 2031 -2.6; 2234 -0.3; 2457 1.5; 2703 2.2; 2973 1.5; 3270 -0.1; 3597 -1.5; 3957 -2.4; 4353 -3.4; 4788 -3.9; 5267 -4.5; 5793 -3.8; 6373 -4.0; 7010 -1.8; 7711 0.2; 8482 -1.6; 9330 -4.5; 10263 -2.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC33iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC33iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.67 | 6.7 dB   |
| Peaking | 256 Hz   | 0.57 | -10.1 dB |
| Peaking | 1659 Hz  | 5.54 | -5.6 dB  |
| Peaking | 5481 Hz  | 2.02 | -4.6 dB  |
| Peaking | 22423 Hz | 2.06 | -1.8 dB  |
| Peaking | 262 Hz   | 3.23 | 1.4 dB   |
| Peaking | 498 Hz   | 1.65 | -2.2 dB  |
| Peaking | 1055 Hz  | 1.18 | 6.2 dB   |
| Peaking | 1657 Hz  | 0.61 | -4.5 dB  |
| Peaking | 2668 Hz  | 2.44 | 5.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-ANC33iS/Audio-Technica%20ATH-ANC33iS.png)