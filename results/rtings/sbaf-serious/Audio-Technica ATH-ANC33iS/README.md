# Audio-Technica ATH-ANC33iS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.3; 37 4.7; 41 4.0; 45 3.3; 49 2.7; 54 2.0; 60 1.1; 66 0.4; 72 -0.1; 79 -0.7; 87 -1.4; 96 -2.3; 106 -3.2; 116 -4.2; 128 -5.1; 141 -5.9; 155 -6.6; 170 -7.1; 187 -7.7; 206 -8.1; 227 -8.4; 249 -8.4; 274 -8.3; 302 -8.3; 332 -8.2; 365 -8.1; 402 -7.8; 442 -7.3; 486 -6.6; 535 -5.8; 588 -4.9; 647 -3.3; 712 -2.3; 783 -0.9; 861 -0.6; 947 -0.4; 1042 0.5; 1146 1.2; 1261 0.2; 1387 -3.0; 1526 -5.8; 1678 -6.0; 1846 -4.4; 2031 -2.2; 2234 0.2; 2457 1.9; 2703 2.8; 2973 2.6; 3270 1.7; 3597 0.6; 3957 -1.2; 4353 -3.4; 4788 -4.0; 5267 -4.1; 5793 -2.4; 6373 -1.5; 7010 0.7; 7711 0.3; 8482 -1.2; 9330 -3.0; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC33iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC33iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.4  | 6.7 dB   |
| Peaking | 339 Hz  | 0.34 | -11.1 dB |
| Peaking | 1445 Hz | 0.48 | 10.8 dB  |
| Peaking | 1650 Hz | 2.07 | -13.9 dB |
| Peaking | 4865 Hz | 1.97 | -6.8 dB  |
| Peaking | 1173 Hz | 9.3  | 1.2 dB   |
| Peaking | 2056 Hz | 6.76 | -1.3 dB  |
| Peaking | 2784 Hz | 4.65 | 1.1 dB   |
| Peaking | 7250 Hz | 6.79 | 1.6 dB   |
| Peaking | 9179 Hz | 6.26 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-ANC33iS/Audio-Technica%20ATH-ANC33iS.png)