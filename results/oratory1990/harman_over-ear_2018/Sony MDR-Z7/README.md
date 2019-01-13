# Sony MDR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 4.7; 25 3.8; 28 2.6; 31 1.7; 34 1.0; 37 0.5; 41 0.2; 45 0.1; 49 0.1; 54 -0.0; 60 -0.2; 66 -0.4; 72 -0.6; 79 -0.7; 87 -1.1; 96 -1.4; 106 -1.7; 116 -1.8; 128 -1.9; 141 -2.0; 155 -2.2; 170 -2.2; 187 -1.8; 206 -1.1; 227 -0.3; 249 0.4; 274 0.9; 302 1.2; 332 1.5; 365 1.7; 402 1.9; 442 1.8; 486 1.5; 535 1.3; 588 1.0; 647 0.4; 712 -0.4; 783 -1.0; 861 -1.2; 947 -0.6; 1042 0.5; 1146 1.9; 1261 3.3; 1387 3.7; 1526 2.9; 1678 1.6; 1846 0.5; 2031 -0.3; 2234 -1.1; 2457 -2.1; 2703 -2.0; 2973 -0.1; 3270 2.9; 3597 5.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.9; 6373 0.4; 7010 -3.2; 7711 -6.4; 8482 -7.6; 9330 -6.3; 10263 -3.0; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.3; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.01 | 5.7 dB  |
| Peaking | 134 Hz   | 1.66 | -2.4 dB |
| Peaking | 1355 Hz  | 4.55 | 4.1 dB  |
| Peaking | 4757 Hz  | 1.91 | 8.0 dB  |
| Peaking | 8295 Hz  | 2.48 | -9.4 dB |
| Peaking | 410 Hz   | 1.55 | 2.1 dB  |
| Peaking | 824 Hz   | 4.36 | -1.9 dB |
| Peaking | 2611 Hz  | 3.41 | -3.8 dB |
| Peaking | 3590 Hz  | 6.11 | 3.5 dB  |
| Peaking | 11598 Hz | 5.75 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-Z7/Sony%20MDR-Z7.png)