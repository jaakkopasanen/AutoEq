# Beyerdynamic T70 250 Ohm sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.7; 28 4.4; 31 4.2; 34 4.0; 37 3.9; 41 3.7; 45 3.6; 49 3.6; 54 3.6; 60 3.6; 66 3.6; 72 3.4; 79 2.7; 87 1.8; 96 0.9; 106 0.2; 116 -0.2; 128 -0.8; 141 -1.1; 155 -0.6; 170 -0.6; 187 -0.9; 206 -0.8; 227 -0.4; 249 -0.4; 274 -0.4; 302 -0.6; 332 -1.0; 365 -1.3; 402 -1.6; 442 -1.8; 486 -1.0; 535 0.0; 588 0.1; 647 -0.0; 712 -0.1; 783 -0.0; 861 -0.1; 947 -0.0; 1042 0.0; 1146 0.0; 1261 0.1; 1387 -0.1; 1526 -0.5; 1678 -0.6; 1846 -0.3; 2031 0.8; 2234 3.2; 2457 4.0; 2703 3.3; 2973 2.3; 3270 2.0; 3597 1.5; 3957 5.8; 4353 3.4; 4788 1.6; 5267 4.2; 5793 5.5; 6373 2.3; 7010 -1.9; 7711 -6.3; 8482 -8.9; 9330 -8.7; 10263 -4.7; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.66 | 4.9 dB   |
| Peaking | 2505 Hz  | 3.95 | 4.3 dB   |
| Peaking | 4042 Hz  | 7.24 | 5.7 dB   |
| Peaking | 5795 Hz  | 3.88 | 6.9 dB   |
| Peaking | 8664 Hz  | 2.83 | -10.6 dB |
| Peaking | 70 Hz    | 1.59 | 3.4 dB   |
| Peaking | 86 Hz    | 0.5  | -1.8 dB  |
| Peaking | 135 Hz   | 3.06 | -0.6 dB  |
| Peaking | 416 Hz   | 3.59 | -1.7 dB  |
| Peaking | 11664 Hz | 6.03 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm%20sample%201/Beyerdynamic%20T70%20250%20Ohm%20sample%201.png)