# A Audio Elite NC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 5.8; 783 3.9; 861 2.3; 947 0.7; 1042 0.0; 1146 -0.4; 1261 0.6; 1387 1.7; 1526 2.8; 1678 3.7; 1846 4.9; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 3.8; 4788 4.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`A Audio Elite NC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.14 | 6.3 dB  |
| Peaking | 508 Hz   | 1.35 | 3.8 dB  |
| Peaking | 2796 Hz  | 1.19 | 6.4 dB  |
| Peaking | 5721 Hz  | 3.07 | 5.2 dB  |
| Peaking | 24000 Hz | 2.36 | 4.3 dB  |
| Peaking | 705 Hz   | 5.04 | 2.3 dB  |
| Peaking | 1084 Hz  | 2.57 | -3.0 dB |
| Peaking | 1902 Hz  | 3.95 | 1.9 dB  |
| Peaking | 6559 Hz  | 6.89 | 2.1 dB  |
| Peaking | 7822 Hz  | 2.24 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20NC%20Active/A%20Audio%20Elite%20NC%20Active.png)