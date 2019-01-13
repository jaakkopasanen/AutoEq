# Sony MDR-AS40EX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 -2.3; 23 -2.6; 25 -2.9; 28 -3.3; 31 -3.6; 34 -3.8; 37 -4.0; 41 -4.2; 45 -4.5; 49 -4.7; 54 -5.0; 60 -5.2; 66 -5.5; 72 -5.8; 79 -6.1; 87 -6.5; 96 -6.5; 106 -6.8; 116 -6.8; 128 -6.9; 141 -7.0; 155 -7.0; 170 -6.9; 187 -6.7; 206 -6.5; 227 -6.1; 249 -5.8; 274 -5.3; 302 -4.6; 332 -4.2; 365 -3.9; 402 -3.4; 442 -2.8; 486 -2.3; 535 -1.8; 588 -1.2; 647 -0.7; 712 -0.0; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -1.1; 1526 -1.7; 1678 -2.3; 1846 -2.2; 2031 -1.2; 2234 -0.1; 2457 1.1; 2703 2.1; 2973 3.1; 3270 3.6; 3597 2.9; 3957 0.1; 4353 -3.5; 4788 -5.0; 5267 -3.1; 5793 -0.6; 6373 0.4; 7010 -0.4; 7711 -3.5; 8482 -6.2; 9330 -3.7; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.8; 16529 -6.3; 18182 -4.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-AS40EX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-AS40EX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 66 Hz    | 0.39 | -4.5 dB |
| Peaking | 192 Hz   | 0.67 | -4.6 dB |
| Peaking | 8475 Hz  | 4.25 | -6.1 dB |
| Peaking | 9568 Hz  | 2.95 | -1.1 dB |
| Peaking | 17083 Hz | 2.34 | -7.3 dB |
| Peaking | 1790 Hz  | 3.01 | -3.1 dB |
| Peaking | 3487 Hz  | 1.6  | 6.1 dB  |
| Peaking | 4589 Hz  | 2.4  | -8.1 dB |
| Peaking | 6202 Hz  | 4.04 | 2.4 dB  |
| Peaking | 10572 Hz | 2.66 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-AS40EX/Sony%20MDR-AS40EX.png)