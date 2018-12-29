# V-Moda XS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 -5.2; 23 -5.5; 25 -5.8; 28 -6.2; 31 -6.4; 34 -6.6; 37 -6.7; 41 -6.8; 45 -6.9; 49 -6.9; 54 -7.1; 60 -7.1; 66 -7.1; 72 -7.3; 79 -7.3; 87 -7.1; 96 -6.7; 106 -6.8; 116 -6.8; 128 -6.9; 141 -6.7; 155 -6.4; 170 -5.8; 187 -5.3; 206 -4.7; 227 -4.9; 249 -4.5; 274 -3.0; 302 -1.6; 332 -0.6; 365 0.1; 402 0.8; 442 1.3; 486 1.8; 535 2.2; 588 2.6; 647 2.6; 712 2.4; 783 2.0; 861 1.3; 947 0.4; 1042 -0.4; 1146 -0.9; 1261 -1.3; 1387 -1.5; 1526 -1.7; 1678 -1.6; 1846 -1.6; 2031 -2.1; 2234 -1.6; 2457 -2.1; 2703 -2.7; 2973 -3.0; 3270 -2.1; 3597 0.6; 3957 3.3; 4353 3.8; 4788 0.5; 5267 3.7; 5793 4.8; 6373 3.3; 7010 0.1; 7711 0.3; 8482 -0.7; 9330 -0.4; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda XS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda XS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.49 | -7.2 dB |
| Peaking | 135 Hz   | 1.43 | -4.4 dB |
| Peaking | 234 Hz   | 4.42 | -2.9 dB |
| Peaking | 5707 Hz  | 4.25 | 5.3 dB  |
| Peaking | 24000 Hz | 2.4  | 2.2 dB  |
| Peaking | 17 Hz    | 1.51 | -1.1 dB |
| Peaking | 615 Hz   | 1.5  | 3.5 dB  |
| Peaking | 2557 Hz  | 0.73 | -2.9 dB |
| Peaking | 4101 Hz  | 5.06 | 5.7 dB  |
| Peaking | 8836 Hz  | 8.04 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20XS/V-Moda%20XS.png)