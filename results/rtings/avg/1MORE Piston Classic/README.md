# 1MORE Piston Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.7; 28 5.1; 31 4.4; 34 3.9; 37 3.4; 41 2.8; 45 2.3; 49 1.8; 54 1.1; 60 0.2; 66 -0.5; 72 -1.2; 79 -1.9; 87 -2.8; 96 -3.6; 106 -4.5; 116 -5.3; 128 -6.1; 141 -6.8; 155 -7.2; 170 -7.5; 187 -7.8; 206 -7.8; 227 -7.8; 249 -7.5; 274 -7.4; 302 -7.2; 332 -6.8; 365 -6.3; 402 -5.7; 442 -5.0; 486 -4.2; 535 -3.2; 588 -2.1; 647 -1.2; 712 -0.3; 783 0.0; 861 -0.0; 947 -0.1; 1042 0.3; 1146 0.8; 1261 1.1; 1387 1.7; 1526 2.5; 1678 3.3; 1846 4.1; 2031 4.7; 2234 5.5; 2457 6.0; 2703 5.5; 2973 3.3; 3270 -0.0; 3597 -2.1; 3957 -2.7; 4353 -3.5; 4788 -3.6; 5267 -3.8; 5793 -3.5; 6373 -2.9; 7010 -0.4; 7711 0.3; 8482 0.0; 9330 -0.8; 10263 -0.7; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.8; 18182 -2.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Piston Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Piston Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.46 | 6.4 dB  |
| Peaking | 205 Hz   | 0.53 | -8.5 dB |
| Peaking | 2642 Hz  | 0.96 | 10.7 dB |
| Peaking | 3928 Hz  | 1.08 | -9.6 dB |
| Peaking | 17964 Hz | 3.42 | -2.4 dB |
| Peaking | 408 Hz   | 2.84 | -0.9 dB |
| Peaking | 709 Hz   | 3.49 | 1.5 dB  |
| Peaking | 4166 Hz  | 6.55 | 1.0 dB  |
| Peaking | 6340 Hz  | 2.44 | -2.4 dB |
| Peaking | 7320 Hz  | 3.7  | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Piston%20Classic/1MORE%20Piston%20Classic.png)