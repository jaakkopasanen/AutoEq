# Audeze LCD-2 Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.9; 116 5.1; 128 4.3; 141 3.5; 155 2.8; 170 2.2; 187 1.6; 206 1.2; 227 1.0; 249 0.9; 274 0.9; 302 0.8; 332 0.9; 365 1.0; 402 1.3; 442 1.7; 486 1.8; 535 1.6; 588 1.1; 647 0.5; 712 -0.2; 783 -0.7; 861 -0.7; 947 0.0; 1042 -0.3; 1146 -0.2; 1261 0.1; 1387 0.8; 1526 2.0; 1678 2.7; 1846 3.6; 2031 5.1; 2234 4.2; 2457 2.7; 2703 3.4; 2973 5.2; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 2.8; 6373 2.3; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -4.4; 13660 -5.1; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.37 | 6.7 dB  |
| Peaking | 487 Hz   | 5.13 | 1.5 dB  |
| Peaking | 2008 Hz  | 4.02 | 3.7 dB  |
| Peaking | 4060 Hz  | 1.25 | 6.7 dB  |
| Peaking | 13102 Hz | 4.89 | -7.2 dB |
| Peaking | 14 Hz    | 2.35 | 1.0 dB  |
| Peaking | 103 Hz   | 4.74 | 1.5 dB  |
| Peaking | 855 Hz   | 2.69 | -1.2 dB |
| Peaking | 8270 Hz  | 5.69 | -1.2 dB |
| Peaking | 15114 Hz | 7.97 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)