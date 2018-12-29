# VSonic VSD3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 -0.1; 23 -0.5; 25 -0.8; 28 -1.2; 31 -1.5; 34 -1.8; 37 -2.0; 41 -2.3; 45 -2.5; 49 -2.7; 54 -3.0; 60 -3.3; 66 -3.6; 72 -3.9; 79 -4.2; 87 -4.6; 96 -5.0; 106 -5.2; 116 -5.2; 128 -5.4; 141 -5.5; 155 -5.5; 170 -5.4; 187 -5.3; 206 -5.2; 227 -4.9; 249 -4.7; 274 -4.3; 302 -4.0; 332 -3.7; 365 -3.3; 402 -3.0; 442 -2.5; 486 -2.3; 535 -1.9; 588 -1.2; 647 -0.9; 712 -0.7; 783 -0.2; 861 -0.2; 947 -0.0; 1042 0.0; 1146 -0.1; 1261 -0.1; 1387 -0.1; 1526 0.1; 1678 0.2; 1846 0.6; 2031 1.1; 2234 1.6; 2457 2.5; 2703 2.7; 2973 3.7; 3270 4.8; 3597 5.4; 3957 4.6; 4353 2.3; 4788 0.7; 5267 -0.4; 5793 -1.6; 6373 -0.6; 7010 1.6; 7711 0.3; 8482 0.0; 9330 -2.5; 10263 -5.3; 11289 -4.4; 12418 -1.2; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 99 Hz    | 0.51 | -3.8 dB |
| Peaking | 234 Hz   | 0.65 | -3.1 dB |
| Peaking | 3526 Hz  | 1.58 | 5.5 dB  |
| Peaking | 5488 Hz  | 3.86 | -2.9 dB |
| Peaking | 10590 Hz | 3.99 | -6.2 dB |
| Peaking | 837 Hz   | 3.73 | 0.5 dB  |
| Peaking | 6189 Hz  | 6.98 | -1.5 dB |
| Peaking | 6976 Hz  | 4.87 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3/VSonic%20VSD3.png)