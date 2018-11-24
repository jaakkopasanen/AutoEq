# Philips Fidelio NC1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -1.9; 23 -1.7; 25 -1.5; 28 -1.2; 31 -0.9; 34 -0.5; 37 -0.2; 41 0.2; 45 0.4; 49 0.5; 54 0.6; 60 0.7; 66 0.8; 72 1.1; 79 1.4; 87 1.6; 96 1.5; 106 1.1; 116 0.7; 128 0.2; 141 -0.3; 155 -0.7; 170 -1.0; 187 -1.3; 206 -1.5; 227 -1.7; 249 -2.0; 274 -1.9; 302 -1.7; 332 -1.6; 365 -1.5; 402 -1.5; 442 -1.5; 486 -1.5; 535 -1.4; 588 -1.2; 647 -1.1; 712 -0.9; 783 -0.7; 861 -0.4; 947 -0.2; 1042 0.1; 1146 0.3; 1261 0.5; 1387 -0.2; 1526 -0.5; 1678 -0.4; 1846 -1.1; 2031 -1.9; 2234 -2.3; 2457 -2.8; 2703 -4.0; 2973 -5.7; 3270 -7.6; 3597 -8.7; 3957 -8.6; 4353 -7.2; 4788 -4.3; 5267 -2.0; 5793 -3.0; 6373 -5.8; 7010 -3.9; 7711 -0.8; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -4.7; 18182 -10.1; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio NC1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio NC1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 2.6  | -1.9 dB  |
| Peaking | 319 Hz   | 1.06 | -2.0 dB  |
| Peaking | 3661 Hz  | 2.01 | -9.3 dB  |
| Peaking | 6500 Hz  | 6.65 | -4.6 dB  |
| Peaking | 18770 Hz | 1.92 | -11.9 dB |
| Peaking | 86 Hz    | 2.11 | 1.9 dB   |
| Peaking | 1221 Hz  | 3.83 | 1.2 dB   |
| Peaking | 5303 Hz  | 8.97 | 1.9 dB   |
| Peaking | 12718 Hz | 0.71 | 2.6 dB   |
| Peaking | 19623 Hz | 0.06 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Philips%20Fidelio%20NC1/Philips%20Fidelio%20NC1.png)