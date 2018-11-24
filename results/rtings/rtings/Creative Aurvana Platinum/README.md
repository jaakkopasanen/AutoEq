# Creative Aurvana Platinum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 -2.0; 23 -3.2; 25 -4.2; 28 -5.4; 31 -6.4; 34 -7.1; 37 -7.7; 41 -8.2; 45 -8.7; 49 -9.0; 54 -9.3; 60 -9.7; 66 -10.1; 72 -10.5; 79 -10.9; 87 -11.4; 96 -11.9; 106 -12.3; 116 -12.7; 128 -13.0; 141 -13.3; 155 -13.5; 170 -13.6; 187 -13.6; 206 -13.4; 227 -13.2; 249 -13.0; 274 -12.9; 302 -12.8; 332 -12.6; 365 -12.6; 402 -12.6; 442 -12.5; 486 -12.0; 535 -10.5; 588 -8.1; 647 -5.4; 712 -3.6; 783 -3.2; 861 -2.5; 947 -0.0; 1042 -0.3; 1146 -1.9; 1261 -3.5; 1387 -4.0; 1526 -3.0; 1678 -1.5; 1846 0.1; 2031 1.7; 2234 3.2; 2457 4.7; 2703 4.6; 2973 3.2; 3270 1.5; 3597 -0.5; 3957 -2.6; 4353 -2.0; 4788 -0.2; 5267 0.1; 5793 -1.6; 6373 -1.5; 7010 -0.4; 7711 -1.5; 8482 -5.6; 9330 -8.9; 10263 -8.3; 11289 -5.5; 12418 -3.4; 13660 -2.4; 15026 -1.6; 16529 -0.1; 18182 0.0; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.35 | -8.7 dB |
| Peaking | 236 Hz  | 0.59 | -8.3 dB |
| Peaking | 460 Hz  | 2.09 | -6.3 dB |
| Peaking | 2562 Hz | 3.67 | 6.0 dB  |
| Peaking | 9919 Hz | 2.23 | -9.3 dB |
| Peaking | 983 Hz  | 4.39 | 2.2 dB  |
| Peaking | 1000 Hz | 3.73 | 0.8 dB  |
| Peaking | 1383 Hz | 3.12 | -3.9 dB |
| Peaking | 3412 Hz | 0.68 | 1.1 dB  |
| Peaking | 4034 Hz | 4.68 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Creative%20Aurvana%20Platinum/Creative%20Aurvana%20Platinum.png)