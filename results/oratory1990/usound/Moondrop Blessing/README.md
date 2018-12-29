# Moondrop Blessing
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 21 -1.6; 23 -2.1; 25 -2.3; 28 -2.2; 31 -2.1; 34 -2.1; 37 -2.1; 41 -2.0; 45 -1.9; 49 -1.8; 54 -1.9; 60 -2.0; 66 -2.2; 72 -2.0; 79 -2.3; 87 -2.1; 96 -1.8; 106 -2.1; 116 -1.8; 128 -2.0; 141 -1.7; 155 -1.7; 170 -1.7; 187 -1.7; 206 -1.7; 227 -1.6; 249 -1.6; 274 -1.5; 302 -1.4; 332 -1.3; 365 -1.2; 402 -1.1; 442 -1.0; 486 -0.9; 535 -0.8; 588 -0.6; 647 -0.5; 712 -0.2; 783 0.1; 861 0.3; 947 0.2; 1042 -0.2; 1146 -1.1; 1261 -1.9; 1387 -2.5; 1526 -2.5; 1678 -2.3; 1846 -2.2; 2031 -2.2; 2234 -2.7; 2457 -3.3; 2703 -3.7; 2973 -3.5; 3270 -2.6; 3597 -2.0; 3957 -1.7; 4353 -1.7; 4788 -1.5; 5267 -1.3; 5793 -0.3; 6373 1.9; 7010 -0.5; 7711 -4.1; 8482 -3.0; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.2; 15026 -4.0; 16529 -6.0; 18182 -6.7; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Moondrop Blessing GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Moondrop Blessing ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.23 | -2.1 dB |
| Peaking | 276 Hz   | 1.24 | -0.8 dB |
| Peaking | 2087 Hz  | 0.92 | -2.2 dB |
| Peaking | 2937 Hz  | 2.15 | -1.9 dB |
| Peaking | 19596 Hz | 0.86 | -9.4 dB |
| Peaking | 916 Hz   | 2.96 | 1.2 dB  |
| Peaking | 1366 Hz  | 4.54 | -1.2 dB |
| Peaking | 6484 Hz  | 7.42 | 3.5 dB  |
| Peaking | 7877 Hz  | 5.11 | -4.4 dB |
| Peaking | 11688 Hz | 2.12 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Moondrop%20Blessing/Moondrop%20Blessing.png)