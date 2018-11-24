# Bluedio T3 Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.5dB
GraphicEQ: 21 -27.4; 23 -27.6; 25 -27.7; 28 -27.8; 31 -27.8; 34 -27.6; 37 -27.5; 41 -27.3; 45 -27.2; 49 -27.1; 54 -27.2; 60 -27.6; 66 -28.0; 72 -28.3; 79 -28.7; 87 -29.2; 96 -29.7; 106 -30.2; 116 -30.6; 128 -31.0; 141 -31.0; 155 -30.8; 170 -30.5; 187 -29.7; 206 -28.5; 227 -27.1; 249 -25.4; 274 -23.3; 302 -20.9; 332 -18.4; 365 -15.6; 402 -12.3; 442 -9.3; 486 -8.4; 535 -8.7; 588 -6.1; 647 -3.5; 712 -5.6; 783 -3.5; 861 -0.5; 947 0.4; 1042 -0.7; 1146 -3.6; 1261 -6.9; 1387 -10.3; 1526 -13.7; 1678 -16.1; 1846 -20.0; 2031 -22.8; 2234 -24.4; 2457 -24.8; 2703 -25.1; 2973 -25.1; 3270 -24.8; 3597 -24.1; 3957 -21.3; 4353 -17.3; 4788 -13.6; 5267 -11.8; 5793 -11.8; 6373 -15.0; 7010 -15.2; 7711 -16.3; 8482 -18.3; 9330 -19.3; 10263 -17.4; 11289 -14.1; 12418 -12.5; 13660 -13.7; 15026 -15.9; 16529 -17.8; 18182 -16.4; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T3 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-4**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T3 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.21 | -26.4 dB |
| Peaking | 163 Hz   | 0.78 | -19.9 dB |
| Peaking | 2598 Hz  | 1.51 | -21.3 dB |
| Peaking | 8946 Hz  | 0.33 | -13.8 dB |
| Peaking | 17702 Hz | 1.29 | -11.3 dB |
| Peaking | 273 Hz   | 2.83 | -4.5 dB  |
| Peaking | 958 Hz   | 1.41 | 8.1 dB   |
| Peaking | 1742 Hz  | 2.31 | -6.8 dB  |
| Peaking | 3649 Hz  | 4.85 | -6.0 dB  |
| Peaking | 5335 Hz  | 4.09 | 5.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bluedio%20T3%20Plus/Bluedio%20T3%20Plus.png)