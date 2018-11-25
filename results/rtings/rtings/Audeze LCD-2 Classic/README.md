# Audeze LCD-2 Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.3; 34 4.8; 37 4.5; 41 4.2; 45 4.1; 49 4.0; 54 3.9; 60 3.8; 66 3.6; 72 3.4; 79 3.1; 87 2.8; 96 2.4; 106 2.0; 116 1.7; 128 1.3; 141 1.0; 155 0.8; 170 0.7; 187 0.7; 206 0.7; 227 0.6; 249 0.5; 274 0.3; 302 0.1; 332 0.0; 365 -0.1; 402 -0.2; 442 -0.2; 486 0.1; 535 0.1; 588 -0.4; 647 -0.9; 712 -1.2; 783 -1.7; 861 -2.0; 947 -0.8; 1042 -0.2; 1146 -0.5; 1261 -0.1; 1387 0.3; 1526 1.8; 1678 1.3; 1846 1.6; 2031 1.3; 2234 3.0; 2457 2.6; 2703 4.5; 2973 4.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.2; 6373 2.1; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  0.79 | 5.7 dB  |
| Peaking | 68 Hz   |  0.84 | 2.5 dB  |
| Peaking | 816 Hz  |  2.63 | -2.2 dB |
| Peaking | 3444 Hz |  1.35 | 5.8 dB  |
| Peaking | 5247 Hz |  3.25 | 4.1 dB  |
| Peaking | 1324 Hz |  5.03 | -0.8 dB |
| Peaking | 1513 Hz |  7.15 | 1.3 dB  |
| Peaking | 6949 Hz | 14.03 | 1.2 dB  |
| Peaking | 8347 Hz |  2.38 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)