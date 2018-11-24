# Audeze LCD2-Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.3; 34 4.8; 37 4.5; 41 4.2; 45 4.1; 49 4.0; 54 3.9; 60 3.8; 66 3.6; 72 3.4; 79 3.1; 87 2.8; 96 2.4; 106 2.0; 116 1.7; 128 1.3; 141 1.0; 155 0.8; 170 0.7; 187 0.7; 206 0.7; 227 0.6; 249 0.5; 274 0.3; 302 0.1; 332 0.0; 365 -0.1; 402 -0.2; 442 -0.2; 486 0.1; 535 0.1; 588 -0.4; 647 -0.9; 712 -1.2; 783 -1.7; 861 -2.0; 947 -0.8; 1042 -0.2; 1146 -0.5; 1261 -0.1; 1387 0.3; 1526 1.8; 1678 1.3; 1846 1.6; 2031 1.3; 2234 3.1; 2457 2.6; 2703 4.2; 2973 4.4; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.5; 5267 5.5; 5793 2.9; 6373 0.9; 7010 2.1; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.9; 18182 -2.5; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD2-Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD2-Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.78 | 5.7 dB  |
| Peaking | 67 Hz    | 0.84 | 2.5 dB  |
| Peaking | 815 Hz   | 2.72 | -2.2 dB |
| Peaking | 3477 Hz  | 1.38 | 5.9 dB  |
| Peaking | 5018 Hz  | 4.13 | 3.3 dB  |
| Peaking | 1355 Hz  | 4.7  | -1.0 dB |
| Peaking | 1516 Hz  | 5.74 | 1.5 dB  |
| Peaking | 19507 Hz | 1.36 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audeze%20LCD2-Classic/Audeze%20LCD2-Classic.png)