# Creative Aurvana Platinum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 -2.0; 23 -3.2; 25 -4.2; 28 -5.4; 31 -6.4; 34 -7.1; 37 -7.7; 41 -8.2; 45 -8.7; 49 -9.0; 54 -9.3; 60 -9.7; 66 -10.1; 72 -10.5; 79 -10.9; 87 -11.4; 96 -11.9; 106 -12.3; 116 -12.7; 128 -13.0; 141 -13.3; 155 -13.5; 170 -13.6; 187 -13.6; 206 -13.4; 227 -13.2; 249 -13.0; 274 -12.9; 302 -12.8; 332 -12.6; 365 -12.6; 402 -12.6; 442 -12.5; 486 -12.0; 535 -10.5; 588 -8.1; 647 -5.4; 712 -3.6; 783 -3.2; 861 -2.5; 947 -0.0; 1042 -0.3; 1146 -1.9; 1261 -3.5; 1387 -4.0; 1526 -3.0; 1678 -1.5; 1846 0.1; 2031 1.7; 2234 3.2; 2457 4.6; 2703 4.3; 2973 2.8; 3270 0.8; 3597 -1.5; 3957 -3.8; 4353 -3.3; 4788 -1.9; 5267 -2.5; 5793 -4.0; 6373 -2.8; 7010 -1.1; 7711 -1.9; 8482 -4.7; 9330 -6.2; 10263 -6.0; 11289 -6.3; 12418 -6.7; 13660 -5.7; 15026 -4.2; 16529 -3.0; 18182 -3.9; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 83 Hz    | 0.35 | -9.3 dB |
| Peaking | 234 Hz   | 0.67 | -7.6 dB |
| Peaking | 458 Hz   | 2.02 | -6.8 dB |
| Peaking | 2581 Hz  | 2.71 | 7.5 dB  |
| Peaking | 19158 Hz | 0.07 | -5.0 dB |
| Peaking | 982 Hz   | 4.64 | 3.0 dB  |
| Peaking | 1371 Hz  | 4.35 | -3.3 dB |
| Peaking | 7250 Hz  | 3.94 | 4.5 dB  |
| Peaking | 11110 Hz | 0.83 | -2.3 dB |
| Peaking | 16432 Hz | 2.13 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Aurvana%20Platinum/Creative%20Aurvana%20Platinum.png)