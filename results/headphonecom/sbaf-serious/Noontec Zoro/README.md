# Noontec Zoro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.2; 23 -1.5; 25 -1.7; 28 -2.0; 31 -2.3; 34 -2.5; 37 -2.6; 41 -2.8; 45 -3.0; 49 -3.1; 54 -3.2; 60 -3.4; 66 -3.7; 72 -3.9; 79 -4.1; 87 -4.2; 96 -4.5; 106 -4.7; 116 -4.7; 128 -4.7; 141 -5.0; 155 -5.4; 170 -5.1; 187 -5.3; 206 -5.3; 227 -5.1; 249 -4.9; 274 -4.4; 302 -4.0; 332 -4.0; 365 -3.9; 402 -3.5; 442 -3.4; 486 -3.3; 535 -3.1; 588 -2.7; 647 -2.1; 712 -1.5; 783 -0.8; 861 -0.3; 947 -0.1; 1042 -0.1; 1146 -0.2; 1261 -0.2; 1387 -1.0; 1526 -1.6; 1678 -1.5; 1846 -0.4; 2031 1.4; 2234 3.5; 2457 5.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.7; 6373 4.3; 7010 2.5; 7711 -1.0; 8482 -4.6; 9330 -4.5; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 67 Hz    | 0.28 | -2.0 dB |
| Peaking | 258 Hz   | 0.32 | -4.0 dB |
| Peaking | 1643 Hz  | 2.03 | -6.1 dB |
| Peaking | 3456 Hz  | 0.42 | 7.6 dB  |
| Peaking | 8836 Hz  | 2.75 | -9.0 dB |
| Peaking | 896 Hz   | 3.91 | 0.5 dB  |
| Peaking | 2538 Hz  | 6.59 | 1.4 dB  |
| Peaking | 3985 Hz  | 1.08 | -0.9 dB |
| Peaking | 5694 Hz  | 2.72 | 1.4 dB  |
| Peaking | 14607 Hz | 1.7  | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Noontec%20Zoro/Noontec%20Zoro.png)