# Stax SR-009 SZ9-1278 after burnin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 4.8; 66 4.4; 72 4.6; 79 4.5; 87 4.4; 96 4.1; 106 4.0; 116 3.9; 128 3.6; 141 3.4; 155 3.2; 170 3.1; 187 3.0; 206 2.9; 227 2.9; 249 2.8; 274 2.6; 302 2.6; 332 2.5; 365 2.5; 402 2.4; 442 2.3; 486 1.8; 535 1.7; 588 1.8; 647 1.4; 712 1.2; 783 1.4; 861 1.3; 947 0.6; 1042 -0.1; 1146 -0.5; 1261 -0.4; 1387 -0.7; 1526 -1.0; 1678 -1.4; 1846 0.2; 2031 1.7; 2234 2.3; 2457 3.9; 2703 3.7; 2973 2.9; 3270 2.7; 3597 3.6; 3957 2.0; 4353 1.0; 4788 -0.5; 5267 1.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 SZ9-1278 after burnin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SZ9-1278 after burnin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.06 | 4.9 dB  |
| Peaking | 2541 Hz  | 2.49 | 6.5 dB  |
| Peaking | 3475 Hz  | 0.69 | -4.1 dB |
| Peaking | 3615 Hz  | 3.33 | 5.7 dB  |
| Peaking | 6034 Hz  | 3.42 | 8.3 dB  |
| Peaking | 34 Hz    | 0.76 | 1.4 dB  |
| Peaking | 168 Hz   | 0.5  | -1.3 dB |
| Peaking | 597 Hz   | 0.39 | 1.1 dB  |
| Peaking | 1421 Hz  | 1.76 | -1.3 dB |
| Peaking | 11930 Hz | 2.26 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SZ9-1278%20after%20burnin/Stax%20SR-009%20SZ9-1278%20after%20burnin.png)