# Sony MDR-ZX770BN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -4.4; 23 -5.1; 25 -5.7; 28 -6.5; 31 -7.1; 34 -7.4; 37 -7.6; 41 -7.7; 45 -7.8; 49 -7.8; 54 -7.7; 60 -7.5; 66 -7.4; 72 -7.2; 79 -7.0; 87 -6.7; 96 -6.5; 106 -6.6; 116 -6.6; 128 -6.7; 141 -6.4; 155 -5.9; 170 -6.2; 187 -7.0; 206 -6.8; 227 -6.4; 249 -6.2; 274 -5.9; 302 -5.4; 332 -4.7; 365 -3.7; 402 -2.6; 442 -1.6; 486 -0.7; 535 0.1; 588 0.1; 647 0.1; 712 -0.2; 783 -0.3; 861 -0.1; 947 -0.1; 1042 -0.2; 1146 -0.7; 1261 -0.7; 1387 -0.5; 1526 -1.1; 1678 -3.0; 1846 -5.8; 2031 -7.8; 2234 -6.9; 2457 -5.1; 2703 -4.0; 2973 -4.2; 3270 -2.6; 3597 1.5; 3957 -5.4; 4353 -9.2; 4788 -10.3; 5267 -8.1; 5793 -3.2; 6373 -1.4; 7010 -2.4; 7711 -6.1; 8482 -9.6; 9330 -10.1; 10263 -9.2; 11289 -8.1; 12418 -6.2; 13660 -5.0; 15026 -7.6; 16529 -11.8; 18182 -12.0; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX770BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-16**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX770BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 67 Hz    |  0.23 | -7.6 dB  |
| Peaking | 2112 Hz  |  3.13 | -7.8 dB  |
| Peaking | 4690 Hz  |  4.29 | -10.3 dB |
| Peaking | 9380 Hz  |  2.17 | -9.0 dB  |
| Peaking | 17724 Hz |  0.79 | -13.0 dB |
| Peaking | 271 Hz   |  0.92 | -6.5 dB  |
| Peaking | 329 Hz   |  0.47 | 4.8 dB   |
| Peaking | 3599 Hz  | 10.35 | 6.4 dB   |
| Peaking | 4478 Hz  |  0.66 | -1.9 dB  |
| Peaking | 6409 Hz  |  3.92 | 4.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX770BN/Sony%20MDR-ZX770BN.png)