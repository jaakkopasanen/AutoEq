# Mpow H5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.1dB
GraphicEQ: 21 -0.9; 23 -1.6; 25 -2.2; 28 -3.0; 31 -3.6; 34 -4.1; 37 -4.5; 41 -4.9; 45 -5.3; 49 -5.7; 54 -6.1; 60 -6.6; 66 -7.2; 72 -7.7; 79 -8.2; 87 -8.8; 96 -9.3; 106 -9.8; 116 -10.2; 128 -10.6; 141 -10.8; 155 -11.0; 170 -11.1; 187 -11.0; 206 -10.8; 227 -10.6; 249 -10.5; 274 -10.1; 302 -10.0; 332 -10.2; 365 -10.0; 402 -9.5; 442 -8.4; 486 -7.1; 535 -5.6; 588 -4.4; 647 -3.4; 712 -2.6; 783 -1.8; 861 -0.8; 947 -0.4; 1042 -0.4; 1146 -2.2; 1261 -4.0; 1387 -5.8; 1526 -6.5; 1678 -6.5; 1846 -6.4; 2031 -6.6; 2234 -5.8; 2457 -5.0; 2703 -5.3; 2973 -6.6; 3270 -8.1; 3597 -9.3; 3957 -8.0; 4353 -5.4; 4788 -3.9; 5267 -3.9; 5793 -1.4; 6373 -2.7; 7010 -6.2; 7711 -7.8; 8482 -10.9; 9330 -13.4; 10263 -12.3; 11289 -9.2; 12418 -6.3; 13660 -5.9; 15026 -8.3; 16529 -9.1; 18182 -8.3; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow H5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow H5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 91 Hz    | 0.47 | -7.2 dB |
| Peaking | 200 Hz   | 0.89 | -6.1 dB |
| Peaking | 386 Hz   | 1.82 | -5.9 dB |
| Peaking | 2201 Hz  | 0.92 | -5.2 dB |
| Peaking | 15015 Hz | 0.24 | -9.1 dB |
| Peaking | 962 Hz   | 4.94 | 2.9 dB  |
| Peaking | 3638 Hz  | 5.93 | -4.3 dB |
| Peaking | 5981 Hz  | 3.74 | 6.0 dB  |
| Peaking | 9495 Hz  | 2.67 | -6.5 dB |
| Peaking | 13021 Hz | 2.86 | 4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20H5/Mpow%20H5.png)