# Shure SE215

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.6; 28 2.5; 31 2.4; 34 2.2; 37 2.1; 41 1.9; 45 1.8; 49 1.6; 54 1.3; 60 0.7; 66 0.1; 72 -0.4; 79 -0.9; 87 -1.6; 96 -2.3; 106 -3.1; 116 -3.8; 128 -4.5; 141 -5.1; 155 -5.6; 170 -5.8; 187 -6.0; 206 -6.2; 227 -6.1; 249 -6.0; 274 -5.8; 302 -5.6; 332 -5.3; 365 -4.9; 402 -4.4; 442 -3.9; 486 -3.3; 535 -2.7; 588 -2.0; 647 -1.2; 712 -0.5; 783 0.1; 861 0.5; 947 0.3; 1042 -0.3; 1146 -1.5; 1261 -1.8; 1387 -2.4; 1526 -2.7; 1678 -3.2; 1846 -3.8; 2031 -4.2; 2234 -3.6; 2457 -1.9; 2703 -0.2; 2973 0.8; 3270 0.9; 3597 0.0; 3957 -1.7; 4353 -5.1; 4788 -7.8; 5267 -4.1; 5793 1.7; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.8; 10263 -4.0; 11289 -3.9; 12418 -1.9; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 226 Hz   | 0.75 | -6.7 dB |
| Peaking | 1900 Hz  | 2.72 | -4.2 dB |
| Peaking | 4814 Hz  | 4.98 | -9.2 dB |
| Peaking | 6351 Hz  | 4.2  | 6.4 dB  |
| Peaking | 10814 Hz | 3.52 | -4.8 dB |
| Peaking | 24 Hz    | 1.17 | 2.9 dB  |
| Peaking | 48 Hz    | 2.15 | 1.7 dB  |
| Peaking | 843 Hz   | 2.4  | 2.6 dB  |
| Peaking | 1093 Hz  | 0.34 | -0.9 dB |
| Peaking | 3120 Hz  | 3.57 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE215/Shure%20SE215.png)