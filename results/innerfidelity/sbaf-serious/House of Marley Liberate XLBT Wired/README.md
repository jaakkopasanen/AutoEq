# House of Marley Liberate XLBT Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.0; 25 -0.1; 28 -0.2; 31 -0.3; 34 -0.3; 37 -0.3; 41 -0.4; 45 -0.5; 49 -0.6; 54 -0.6; 60 -0.7; 66 -0.9; 72 -1.1; 79 -1.4; 87 -1.6; 96 -1.9; 106 -2.1; 116 -2.2; 128 -2.4; 141 -2.8; 155 -3.0; 170 -3.0; 187 -3.1; 206 -3.4; 227 -3.8; 249 -3.9; 274 -3.9; 302 -3.8; 332 -3.7; 365 -3.4; 402 -2.9; 442 -1.8; 486 -0.7; 535 0.6; 588 2.6; 647 3.8; 712 3.5; 783 2.8; 861 1.2; 947 0.2; 1042 -0.4; 1146 -0.9; 1261 -1.1; 1387 -1.1; 1526 -0.7; 1678 0.7; 1846 1.9; 2031 5.3; 2234 5.9; 2457 4.4; 2703 4.3; 2973 4.9; 3270 5.2; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Liberate XLBT Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Liberate XLBT Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 446 Hz  | 0.32 | -5.4 dB |
| Peaking | 670 Hz  | 1.54 | 8.6 dB  |
| Peaking | 1633 Hz | 1.65 | -4.2 dB |
| Peaking | 2078 Hz | 1.29 | 7.8 dB  |
| Peaking | 4758 Hz | 1.39 | 6.2 dB  |
| Peaking | 3540 Hz | 4.56 | 1.6 dB  |
| Peaking | 4742 Hz | 3.95 | -0.8 dB |
| Peaking | 6410 Hz | 3.07 | 4.1 dB  |
| Peaking | 6508 Hz | 0.54 | -0.7 dB |
| Peaking | 7444 Hz | 2.54 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Liberate%20XLBT%20Wired/House%20of%20Marley%20Liberate%20XLBT%20Wired.png)