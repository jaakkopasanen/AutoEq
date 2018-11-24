# B&O PLAY E8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.3; 28 1.9; 31 1.5; 34 1.3; 37 1.2; 41 1.2; 45 1.4; 49 1.6; 54 1.8; 60 1.9; 66 2.1; 72 2.3; 79 2.4; 87 2.4; 96 2.3; 106 1.9; 116 1.5; 128 0.8; 141 0.2; 155 -0.5; 170 -1.3; 187 -2.1; 206 -2.8; 227 -3.4; 249 -3.7; 274 -4.0; 302 -4.0; 332 -4.0; 365 -3.7; 402 -3.4; 442 -3.0; 486 -2.4; 535 -1.8; 588 -1.1; 647 -0.2; 712 0.6; 783 1.2; 861 1.2; 947 0.5; 1042 -0.4; 1146 -1.3; 1261 -1.7; 1387 -1.9; 1526 -1.9; 1678 -1.8; 1846 -1.2; 2031 0.9; 2234 3.3; 2457 4.1; 2703 3.9; 2973 3.4; 3270 3.0; 3597 3.5; 3957 4.0; 4353 3.4; 4788 3.1; 5267 2.7; 5793 0.4; 6373 -5.6; 7010 -9.5; 7711 -6.5; 8482 -4.3; 9330 -8.0; 10263 -11.1; 11289 -6.0; 12418 -0.1; 13660 0.0; 15026 0.0; 16529 -0.5; 18182 -2.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`B&O PLAY E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `B&O PLAY E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 314 Hz   | 1.42 | -4.6 dB  |
| Peaking | 2567 Hz  | 4.16 | 3.7 dB   |
| Peaking | 4746 Hz  | 1.4  | 5.2 dB   |
| Peaking | 6945 Hz  | 3.62 | -11.2 dB |
| Peaking | 10159 Hz | 4.05 | -11.7 dB |
| Peaking | 11 Hz    | 1.3  | 2.6 dB   |
| Peaking | 15 Hz    | 0.46 | 2.2 dB   |
| Peaking | 85 Hz    | 1.65 | 2.7 dB   |
| Peaking | 1517 Hz  | 3.22 | -2.7 dB  |
| Peaking | 17960 Hz | 4.59 | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/B&O%20PLAY%20E8/B&O%20PLAY%20E8.png)