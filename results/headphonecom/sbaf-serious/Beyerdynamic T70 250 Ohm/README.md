# Beyerdynamic T70 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 1.2; 28 1.0; 31 0.9; 34 0.8; 37 0.6; 41 0.5; 45 0.4; 49 0.4; 54 0.2; 60 0.1; 66 0.1; 72 0.0; 79 0.1; 87 0.2; 96 -0.2; 106 -1.0; 116 -1.7; 128 -2.3; 141 -2.7; 155 -2.5; 170 -1.5; 187 -2.1; 206 -1.7; 227 -1.0; 249 -0.6; 274 -0.4; 302 -0.4; 332 -0.6; 365 -0.8; 402 -1.2; 442 -1.5; 486 -1.4; 535 0.1; 588 0.0; 647 -0.0; 712 -0.0; 783 -0.1; 861 -0.1; 947 -0.1; 1042 0.1; 1146 0.1; 1261 0.1; 1387 -0.3; 1526 -0.6; 1678 -0.6; 1846 0.3; 2031 1.2; 2234 2.7; 2457 3.2; 2703 2.5; 2973 2.6; 3270 2.3; 3597 2.1; 3957 6.0; 4353 4.2; 4788 3.2; 5267 5.9; 5793 6.0; 6373 5.2; 7010 -1.9; 7711 -6.2; 8482 -8.0; 9330 -7.2; 10263 -1.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 155 Hz   | 1.52 | -2.5 dB  |
| Peaking | 2505 Hz  | 3.35 | 3.1 dB   |
| Peaking | 4040 Hz  | 5.28 | 5.0 dB   |
| Peaking | 5831 Hz  | 2.9  | 8.1 dB   |
| Peaking | 8325 Hz  | 2.78 | -10.2 dB |
| Peaking | 11 Hz    | 0.31 | 1.6 dB   |
| Peaking | 443 Hz   | 4.77 | -1.6 dB  |
| Peaking | 1644 Hz  | 3.47 | -1.6 dB  |
| Peaking | 1872 Hz  | 1.65 | 0.6 dB   |
| Peaking | 11093 Hz | 6.75 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm/Beyerdynamic%20T70%20250%20Ohm.png)