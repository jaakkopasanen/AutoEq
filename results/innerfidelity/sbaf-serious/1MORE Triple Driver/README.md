# 1MORE Triple Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.6; 25 -2.0; 28 -2.6; 31 -3.0; 34 -3.4; 37 -3.7; 41 -4.0; 45 -4.3; 49 -4.6; 54 -4.9; 60 -5.2; 66 -5.5; 72 -5.8; 79 -6.1; 87 -6.4; 96 -6.7; 106 -6.8; 116 -6.8; 128 -6.9; 141 -6.8; 155 -6.7; 170 -6.6; 187 -6.3; 206 -6.0; 227 -5.5; 249 -5.2; 274 -4.7; 302 -4.2; 332 -3.7; 365 -3.1; 402 -2.6; 442 -1.9; 486 -1.5; 535 -1.0; 588 -0.3; 647 0.1; 712 0.3; 783 0.6; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.2; 1261 -0.5; 1387 -1.4; 1526 -2.2; 1678 -3.0; 1846 -3.6; 2031 -4.0; 2234 -4.6; 2457 -4.5; 2703 -4.2; 2973 -2.5; 3270 -0.8; 3597 -0.6; 3957 -3.0; 4353 -5.4; 4788 -2.8; 5267 3.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -3.2; 10263 -3.6; 11289 -0.5; 12418 0.0; 13660 0.0; 15026 -3.3; 16529 -4.7; 18182 -2.3; 20000 -0.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.48 | -5.7 dB |
| Peaking | 205 Hz   | 0.96 | -3.4 dB |
| Peaking | 2252 Hz  | 1.94 | -4.9 dB |
| Peaking | 4443 Hz  | 5.46 | -6.9 dB |
| Peaking | 5812 Hz  | 3.77 | 7.9 dB  |
| Peaking | 800 Hz   | 2.09 | 1.4 dB  |
| Peaking | 1630 Hz  | 5.49 | -1.1 dB |
| Peaking | 9892 Hz  | 3.22 | -6.1 dB |
| Peaking | 12500 Hz | 0.77 | 3.1 dB  |
| Peaking | 16278 Hz | 1.55 | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Triple%20Driver/1MORE%20Triple%20Driver.png)