# Apple AirPods

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 4.6; 45 3.2; 49 2.0; 54 0.7; 60 -0.5; 66 -1.4; 72 -2.0; 79 -2.4; 87 -2.7; 96 -2.9; 106 -3.0; 116 -3.0; 128 -2.9; 141 -2.8; 155 -2.6; 170 -2.4; 187 -2.3; 206 -2.1; 227 -1.9; 249 -1.8; 274 -1.7; 302 -1.6; 332 -1.6; 365 -1.6; 402 -1.6; 442 -1.5; 486 -1.4; 535 -1.2; 588 -1.1; 647 -0.8; 712 -0.3; 783 0.1; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.8; 1261 -1.8; 1387 -3.1; 1526 -4.7; 1678 -5.9; 1846 -6.8; 2031 -7.1; 2234 -6.3; 2457 -5.3; 2703 -4.7; 2973 -4.2; 3270 -3.4; 3597 -3.0; 3957 -3.1; 4353 -3.6; 4788 -3.2; 5267 -2.9; 5793 -3.2; 6373 -3.4; 7010 -3.1; 7711 -3.1; 8482 -5.1; 9330 -7.7; 10263 -6.2; 11289 -1.5; 12418 -1.0; 13660 -4.5; 15026 -3.5; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple AirPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple AirPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 1.92 | 7.4 dB  |
| Peaking | 1974 Hz  | 1.72 | -6.7 dB |
| Peaking | 4958 Hz  | 0.77 | -2.7 dB |
| Peaking | 9508 Hz  | 3.9  | -7.2 dB |
| Peaking | 14144 Hz | 5.05 | -5.0 dB |
| Peaking | 20 Hz    | 2.49 | 5.5 dB  |
| Peaking | 41 Hz    | 1.82 | 5.5 dB  |
| Peaking | 43 Hz    | 0.15 | -3.7 dB |
| Peaking | 936 Hz   | 2.8  | 1.7 dB  |
| Peaking | 16739 Hz | 4.71 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Apple%20AirPods/Apple%20AirPods.png)