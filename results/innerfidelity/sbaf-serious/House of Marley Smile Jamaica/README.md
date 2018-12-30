# House of Marley Smile Jamaica
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.2; 23 -10.3; 25 -10.4; 28 -10.5; 31 -10.6; 34 -10.7; 37 -10.8; 41 -10.9; 45 -11.0; 49 -11.2; 54 -11.4; 60 -11.6; 66 -11.8; 72 -12.1; 79 -12.3; 87 -12.6; 96 -12.8; 106 -12.9; 116 -13.0; 128 -13.0; 141 -13.0; 155 -12.9; 170 -12.8; 187 -12.5; 206 -12.2; 227 -11.7; 249 -11.2; 274 -10.7; 302 -10.0; 332 -9.4; 365 -8.7; 402 -7.9; 442 -7.0; 486 -6.3; 535 -5.4; 588 -4.2; 647 -2.9; 712 -1.9; 783 -1.4; 861 -0.8; 947 -0.2; 1042 0.3; 1146 0.9; 1261 0.9; 1387 -0.3; 1526 -2.4; 1678 -3.6; 1846 -3.1; 2031 -1.4; 2234 0.4; 2457 2.9; 2703 5.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 2.9; 4788 -0.8; 5267 -4.8; 5793 -0.1; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Smile Jamaica GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Smile Jamaica ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.19 | -9.9 dB |
| Peaking | 163 Hz   | 0.6  | -7.1 dB |
| Peaking | 354 Hz   | 1.13 | -3.9 dB |
| Peaking | 3299 Hz  | 2.62 | 7.3 dB  |
| Peaking | 21887 Hz | 2.3  | 1.6 dB  |
| Peaking | 1218 Hz  | 1.69 | 2.4 dB  |
| Peaking | 1695 Hz  | 3.38 | -5.1 dB |
| Peaking | 4065 Hz  | 6.17 | 3.1 dB  |
| Peaking | 5300 Hz  | 4.78 | -7.2 dB |
| Peaking | 6342 Hz  | 5.48 | 6.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Smile%20Jamaica/House%20of%20Marley%20Smile%20Jamaica.png)