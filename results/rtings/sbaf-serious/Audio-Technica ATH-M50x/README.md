# Audio-Technica ATH-M50x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.4; 25 0.0; 28 -0.5; 31 -0.9; 34 -1.2; 37 -1.3; 41 -1.5; 45 -1.5; 49 -1.4; 54 -1.1; 60 -0.7; 66 -0.3; 72 -0.2; 79 -0.4; 87 -1.0; 96 -1.5; 106 -1.9; 116 -2.0; 128 -2.1; 141 -2.1; 155 -2.1; 170 -1.8; 187 -1.3; 206 -0.5; 227 0.7; 249 2.2; 274 3.7; 302 4.3; 332 4.2; 365 4.1; 402 3.1; 442 2.2; 486 1.7; 535 1.3; 588 1.0; 647 0.9; 712 0.7; 783 0.4; 861 0.1; 947 -0.0; 1042 0.1; 1146 0.4; 1261 0.4; 1387 -0.1; 1526 -0.5; 1678 -1.2; 1846 -2.2; 2031 -2.5; 2234 -1.7; 2457 -0.8; 2703 0.2; 2973 1.2; 3270 3.2; 3597 4.3; 3957 1.0; 4353 -2.5; 4788 0.9; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 209 Hz  | 0.7  | -6.8 dB  |
| Peaking | 292 Hz  | 0.98 | 9.7 dB   |
| Peaking | 3611 Hz | 2.3  | 13.9 dB  |
| Peaking | 4268 Hz | 1.24 | -17.7 dB |
| Peaking | 5501 Hz | 1.79 | 15.0 dB  |
| Peaking | 18 Hz   | 1.19 | 1.8 dB   |
| Peaking | 38 Hz   | 0.83 | -1.6 dB  |
| Peaking | 70 Hz   | 2.73 | 1.4 dB   |
| Peaking | 1270 Hz | 3.19 | 1.0 dB   |
| Peaking | 1945 Hz | 6.06 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-M50x/Audio-Technica%20ATH-M50x.png)