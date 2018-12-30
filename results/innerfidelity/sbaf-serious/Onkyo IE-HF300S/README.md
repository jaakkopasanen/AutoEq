# Onkyo IE-HF300S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.3; 28 -1.7; 31 -2.0; 34 -2.3; 37 -2.6; 41 -2.9; 45 -3.1; 49 -3.4; 54 -3.7; 60 -4.0; 66 -4.3; 72 -4.6; 79 -4.9; 87 -5.3; 96 -5.7; 106 -6.0; 116 -6.0; 128 -6.2; 141 -6.4; 155 -6.4; 170 -6.3; 187 -6.1; 206 -6.0; 227 -5.6; 249 -5.4; 274 -5.0; 302 -4.6; 332 -4.1; 365 -3.5; 402 -3.1; 442 -2.5; 486 -2.0; 535 -1.5; 588 -0.7; 647 -0.4; 712 -0.2; 783 0.4; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.3; 1261 -0.6; 1387 -1.1; 1526 -1.6; 1678 -1.8; 1846 -1.3; 2031 -0.6; 2234 0.4; 2457 1.8; 2703 3.1; 2973 4.6; 3270 5.8; 3597 5.6; 3957 4.0; 4353 0.8; 4788 -1.3; 5267 -0.9; 5793 0.7; 6373 2.8; 7010 2.5; 7711 0.3; 8482 -0.7; 9330 -1.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Onkyo IE-HF300S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo IE-HF300S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 103 Hz   | 0.49 | -5.1 dB |
| Peaking | 236 Hz   | 0.95 | -3.0 dB |
| Peaking | 1699 Hz  | 3.34 | -2.3 dB |
| Peaking | 3297 Hz  | 2.72 | 6.5 dB  |
| Peaking | 22050 Hz | 2.17 | 0.9 dB  |
| Peaking | 796 Hz   | 2.99 | 1.1 dB  |
| Peaking | 3906 Hz  | 6.42 | 2.0 dB  |
| Peaking | 4858 Hz  | 3.19 | -2.9 dB |
| Peaking | 6559 Hz  | 4.84 | 3.7 dB  |
| Peaking | 8904 Hz  | 6.78 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Onkyo%20IE-HF300S/Onkyo%20IE-HF300S.png)