# Monster Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -8.4; 23 -8.3; 25 -8.2; 28 -8.1; 31 -7.9; 34 -7.8; 37 -7.7; 41 -7.5; 45 -7.3; 49 -7.2; 54 -7.1; 60 -6.9; 66 -6.8; 72 -6.7; 79 -6.7; 87 -6.6; 96 -6.5; 106 -6.3; 116 -6.0; 128 -5.8; 141 -5.7; 155 -5.3; 170 -5.0; 187 -4.6; 206 -4.3; 227 -3.8; 249 -3.3; 274 -2.9; 302 -2.4; 332 -2.0; 365 -1.6; 402 -1.1; 442 -0.6; 486 -0.4; 535 0.0; 588 0.6; 647 0.8; 712 0.9; 783 1.1; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.1; 1387 -1.5; 1526 -2.8; 1678 -3.6; 1846 -4.3; 2031 -4.9; 2234 -5.2; 2457 -4.7; 2703 -4.1; 2973 -0.9; 3270 2.1; 3597 3.5; 3957 2.8; 4353 0.1; 4788 -1.6; 5267 -1.1; 5793 1.1; 6373 3.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.9; 16529 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.21 | -8.1 dB |
| Peaking | 152 Hz   | 0.89 | -2.9 dB |
| Peaking | 2246 Hz  | 1.64 | -5.9 dB |
| Peaking | 3536 Hz  | 4.32 | 5.8 dB  |
| Peaking | 6564 Hz  | 7.18 | 4.8 dB  |
| Peaking | 285 Hz   | 1.94 | -0.7 dB |
| Peaking | 725 Hz   | 1.54 | 1.7 dB  |
| Peaking | 1611 Hz  | 4.94 | -1.0 dB |
| Peaking | 4925 Hz  | 7.64 | -2.1 dB |
| Peaking | 15153 Hz | 7    | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)