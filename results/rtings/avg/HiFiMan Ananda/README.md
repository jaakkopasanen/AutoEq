# HiFiMan Ananda

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.2; 28 3.8; 31 3.5; 34 3.2; 37 3.0; 41 2.7; 45 2.4; 49 2.2; 54 1.9; 60 1.6; 66 1.3; 72 1.1; 79 0.9; 87 0.7; 96 0.5; 106 0.1; 116 -0.2; 128 -0.5; 141 -0.7; 155 -1.0; 170 -1.2; 187 -1.3; 206 -1.2; 227 -1.3; 249 -1.2; 274 -1.1; 302 -0.7; 332 -0.0; 365 -0.4; 402 -1.3; 442 -1.7; 486 -1.7; 535 -1.8; 588 -2.1; 647 -0.8; 712 0.6; 783 0.8; 861 0.1; 947 -0.6; 1042 0.6; 1146 2.4; 1261 2.1; 1387 1.6; 1526 2.6; 1678 3.2; 1846 2.2; 2031 1.2; 2234 0.9; 2457 -0.4; 2703 -0.9; 2973 -2.3; 3270 -1.8; 3597 -1.7; 3957 -1.3; 4353 -1.4; 4788 -0.5; 5267 1.5; 5793 2.3; 6373 -2.3; 7010 -2.4; 7711 -2.3; 8482 -2.3; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 -1.2; 13660 -2.5; 15026 -2.3; 16529 -1.7; 18182 -3.8; 20000 -14.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Ananda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Ananda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.24 | 4.9 dB   |
| Peaking | 867 Hz   | 0.08 | -1.4 dB  |
| Peaking | 1190 Hz  | 1.78 | 2.7 dB   |
| Peaking | 1733 Hz  | 2.75 | 3.6 dB   |
| Peaking | 20137 Hz | 1.94 | -14.1 dB |
| Peaking | 2277 Hz  | 6.83 | 1.0 dB   |
| Peaking | 3128 Hz  | 3.38 | -1.4 dB  |
| Peaking | 5665 Hz  | 5.06 | 5.4 dB   |
| Peaking | 6574 Hz  | 3.31 | -3.0 dB  |
| Peaking | 13916 Hz | 5.57 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Ananda/HiFiMan%20Ananda.png)