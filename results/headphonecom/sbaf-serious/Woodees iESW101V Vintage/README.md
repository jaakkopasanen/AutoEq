# Woodees iESW101V Vintage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -7.1; 23 -7.1; 25 -7.0; 28 -6.9; 31 -6.7; 34 -6.6; 37 -6.5; 41 -6.3; 45 -6.2; 49 -6.1; 54 -6.1; 60 -6.0; 66 -6.0; 72 -5.9; 79 -5.9; 87 -5.9; 96 -5.8; 106 -5.7; 116 -5.5; 128 -5.5; 141 -5.5; 155 -5.4; 170 -5.2; 187 -5.0; 206 -4.8; 227 -4.5; 249 -4.3; 274 -4.0; 302 -3.6; 332 -3.1; 365 -2.7; 402 -2.2; 442 -1.9; 486 -1.4; 535 -1.0; 588 -0.5; 647 -0.0; 712 0.3; 783 0.7; 861 0.6; 947 0.3; 1042 1.1; 1146 1.5; 1261 0.7; 1387 0.0; 1526 -0.7; 1678 -1.2; 1846 -1.4; 2031 -1.6; 2234 -1.8; 2457 -1.8; 2703 -1.3; 2973 0.6; 3270 3.3; 3597 5.4; 3957 4.9; 4353 2.5; 4788 0.3; 5267 -2.8; 5793 -6.8; 6373 0.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW101V Vintage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW101V Vintage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.13 | -6.7 dB |
| Peaking | 209 Hz  | 0.91 | -2.7 dB |
| Peaking | 2603 Hz | 2    | -4.3 dB |
| Peaking | 3591 Hz | 2    | 6.9 dB  |
| Peaking | 5656 Hz | 7.61 | -8.6 dB |
| Peaking | 383 Hz  | 1.93 | -0.7 dB |
| Peaking | 1270 Hz | 0.97 | 2.5 dB  |
| Peaking | 1641 Hz | 1.85 | -2.7 dB |
| Peaking | 6256 Hz | 2.16 | -1.7 dB |
| Peaking | 6785 Hz | 6.62 | 4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW101V%20Vintage/Woodees%20iESW101V%20Vintage.png)