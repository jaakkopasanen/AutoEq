# Oppo PM-3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -1.5; 23 -1.3; 25 -1.1; 28 -0.8; 31 -0.5; 34 -0.2; 37 -0.0; 41 0.2; 45 0.2; 49 0.3; 54 0.1; 60 -0.2; 66 -0.8; 72 -1.4; 79 -2.0; 87 -2.6; 96 -3.1; 106 -3.5; 116 -3.9; 128 -4.2; 141 -4.4; 155 -4.5; 170 -4.3; 187 -4.0; 206 -3.6; 227 -3.1; 249 -2.5; 274 -2.0; 302 -1.4; 332 -1.0; 365 -0.8; 402 -1.0; 442 -1.3; 486 -1.8; 535 -2.4; 588 -3.0; 647 -2.9; 712 -2.5; 783 -1.9; 861 -1.1; 947 -0.3; 1042 -0.1; 1146 -1.1; 1261 -2.0; 1387 -2.5; 1526 -3.0; 1678 -3.4; 1846 -4.4; 2031 -4.3; 2234 -5.0; 2457 -4.6; 2703 -4.3; 2973 -3.7; 3270 -3.0; 3597 -2.3; 3957 -1.6; 4353 -2.0; 4788 0.1; 5267 2.7; 5793 3.2; 6373 -2.1; 7010 -7.2; 7711 -7.9; 8482 -10.2; 9330 -11.9; 10263 -6.8; 11289 -0.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 148 Hz   | 0.97 | -4.7 dB  |
| Peaking | 615 Hz   | 3.06 | -2.7 dB  |
| Peaking | 2265 Hz  | 1.17 | -4.8 dB  |
| Peaking | 5500 Hz  | 5.43 | 6.7 dB   |
| Peaking | 8694 Hz  | 2.43 | -12.2 dB |
| Peaking | 17 Hz    | 0.29 | -1.5 dB  |
| Peaking | 47 Hz    | 1.37 | 2.0 dB   |
| Peaking | 1003 Hz  | 7.61 | 1.4 dB   |
| Peaking | 9824 Hz  | 6.52 | -4.6 dB  |
| Peaking | 11377 Hz | 2.61 | 3.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Oppo%20PM-3/Oppo%20PM-3.png)