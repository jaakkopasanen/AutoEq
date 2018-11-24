# Panasonic RP-HC800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 21 -12.9; 23 -12.8; 25 -12.8; 28 -12.7; 31 -12.7; 34 -12.7; 37 -12.6; 41 -12.5; 45 -12.4; 49 -12.4; 54 -12.2; 60 -12.1; 66 -12.0; 72 -11.9; 79 -11.8; 87 -11.8; 96 -11.9; 106 -12.0; 116 -12.2; 128 -12.3; 141 -12.4; 155 -12.5; 170 -12.5; 187 -12.4; 206 -12.3; 227 -12.0; 249 -11.7; 274 -11.3; 302 -10.9; 332 -10.5; 365 -10.0; 402 -9.5; 442 -9.0; 486 -8.2; 535 -7.0; 588 -5.7; 647 -3.5; 712 -0.9; 783 0.4; 861 0.2; 947 0.2; 1042 -0.7; 1146 -1.9; 1261 -2.7; 1387 -2.4; 1526 -2.4; 1678 -2.5; 1846 -3.7; 2031 -4.3; 2234 -5.8; 2457 -5.9; 2703 -2.6; 2973 0.3; 3270 -0.2; 3597 -0.6; 3957 -2.5; 4353 -6.3; 4788 -6.7; 5267 -4.9; 5793 -6.8; 6373 -10.7; 7010 -6.5; 7711 -4.6; 8482 -8.4; 9330 -10.9; 10263 -9.2; 11289 -7.0; 12418 -4.8; 13660 -3.9; 15026 -5.7; 16529 -5.7; 18182 -3.4; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.12 | -12.5 dB |
| Peaking | 281 Hz   | 0.77 | -6.7 dB  |
| Peaking | 2223 Hz  | 4.27 | -4.8 dB  |
| Peaking | 8628 Hz  | 0.71 | -8.6 dB  |
| Peaking | 21683 Hz | 0.52 | -7.2 dB  |
| Peaking | 840 Hz   | 2.39 | 5.1 dB   |
| Peaking | 2228 Hz  | 0.21 | -2.0 dB  |
| Peaking | 3363 Hz  | 1.92 | 5.1 dB   |
| Peaking | 4432 Hz  | 5.94 | -3.3 dB  |
| Peaking | 7646 Hz  | 8.22 | 5.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Panasonic%20RP-HC800/Panasonic%20RP-HC800.png)