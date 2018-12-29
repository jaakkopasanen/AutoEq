# Sennheiser IE 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.1; 28 -4.1; 31 -4.2; 34 -4.2; 37 -4.2; 41 -4.2; 45 -4.2; 49 -4.1; 54 -4.1; 60 -4.1; 66 -4.1; 72 -4.2; 79 -4.2; 87 -4.2; 96 -4.3; 106 -4.3; 116 -4.3; 128 -4.3; 141 -4.3; 155 -4.0; 170 -3.5; 187 -3.0; 206 -2.4; 227 -2.8; 249 -3.8; 274 -3.1; 302 -2.2; 332 -1.4; 365 -1.0; 402 -0.6; 442 -0.1; 486 0.4; 535 0.9; 588 1.1; 647 1.2; 712 1.3; 783 1.3; 861 1.0; 947 0.4; 1042 -0.3; 1146 -0.7; 1261 -0.7; 1387 -0.4; 1526 -0.3; 1678 0.3; 1846 1.6; 2031 3.1; 2234 4.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.5; 5267 1.1; 5793 0.5; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -1.2; 13660 -5.2; 15026 -6.9; 16529 -5.1; 18182 -3.1; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 31 Hz    |  0.28 | -4.0 dB  |
| Peaking | 154 Hz   |  0.78 | -2.6 dB  |
| Peaking | 3356 Hz  |  1.12 | 7.0 dB   |
| Peaking | 12906 Hz |  0.68 | 13.9 dB  |
| Peaking | 14282 Hz |  0.73 | -19.1 dB |
| Peaking | 265 Hz   |  5.34 | -1.8 dB  |
| Peaking | 740 Hz   |  0.97 | 3.5 dB   |
| Peaking | 1316 Hz  |  0.58 | -3.5 dB  |
| Peaking | 2320 Hz  |  2.45 | 3.4 dB   |
| Peaking | 6541 Hz  | 11.37 | 4.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20IE%20800%20S/Sennheiser%20IE%20800%20S.png)