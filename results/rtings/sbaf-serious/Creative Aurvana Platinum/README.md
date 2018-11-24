# Creative Aurvana Platinum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -1.6; 23 -2.8; 25 -3.9; 28 -5.3; 31 -6.3; 34 -7.1; 37 -7.8; 41 -8.4; 45 -8.9; 49 -9.3; 54 -9.6; 60 -10.0; 66 -10.3; 72 -10.5; 79 -10.7; 87 -11.1; 96 -11.4; 106 -11.9; 116 -12.2; 128 -12.5; 141 -12.8; 155 -12.9; 170 -12.9; 187 -13.0; 206 -12.9; 227 -12.7; 249 -12.5; 274 -12.2; 302 -12.0; 332 -11.7; 365 -11.6; 402 -11.5; 442 -11.4; 486 -10.8; 535 -9.3; 588 -7.1; 647 -4.3; 712 -2.8; 783 -2.7; 861 -2.4; 947 -0.0; 1042 -0.3; 1146 -1.7; 1261 -3.2; 1387 -4.1; 1526 -3.4; 1678 -1.8; 1846 0.1; 2031 2.1; 2234 3.7; 2457 5.1; 2703 5.2; 2973 4.3; 3270 3.4; 3597 1.7; 3957 -1.4; 4353 -2.0; 4788 -0.3; 5267 0.5; 5793 -0.1; 6373 1.0; 7010 2.0; 7711 -0.5; 8482 -5.3; 9330 -7.4; 10263 -4.9; 11289 -1.0; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 114 Hz  | 0.33 | -12.1 dB |
| Peaking | 381 Hz  | 1.17 | -6.2 dB  |
| Peaking | 1468 Hz | 4.76 | -3.9 dB  |
| Peaking | 2575 Hz | 2.3  | 6.2 dB   |
| Peaking | 9346 Hz | 4.44 | -8.4 dB  |
| Peaking | 513 Hz  | 4.72 | -2.2 dB  |
| Peaking | 697 Hz  | 4.88 | 1.9 dB   |
| Peaking | 978 Hz  | 7.03 | 2.9 dB   |
| Peaking | 4235 Hz | 7.29 | -3.2 dB  |
| Peaking | 6962 Hz | 7    | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Creative%20Aurvana%20Platinum/Creative%20Aurvana%20Platinum.png)