# Beyerdynamic DT 770 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.5; 23 -2.9; 25 -3.3; 28 -3.7; 31 -4.1; 34 -4.4; 37 -4.6; 41 -4.9; 45 -5.0; 49 -5.1; 54 -5.1; 60 -4.7; 66 -3.7; 72 -1.4; 79 2.2; 87 -1.0; 96 -5.6; 106 -6.7; 116 -6.5; 128 -5.9; 141 -4.5; 155 -2.4; 170 -1.0; 187 0.1; 206 1.7; 227 2.1; 249 1.8; 274 1.1; 302 0.7; 332 0.4; 365 0.3; 402 0.3; 442 0.2; 486 0.4; 535 0.5; 588 0.8; 647 1.2; 712 1.1; 783 0.9; 861 0.3; 947 -0.1; 1042 0.0; 1146 0.5; 1261 0.6; 1387 0.5; 1526 0.0; 1678 -0.4; 1846 -0.8; 2031 -1.3; 2234 -1.8; 2457 -1.6; 2703 -0.3; 2973 1.7; 3270 4.1; 3597 6.0; 3957 5.2; 4353 0.1; 4788 -1.4; 5267 0.0; 5793 -2.0; 6373 -6.0; 7010 -5.1; 7711 -5.3; 8482 -6.6; 9330 -6.5; 10263 -4.2; 11289 -3.6; 12418 -4.1; 13660 -1.8; 15026 0.0; 16529 -3.0; 18182 -6.4; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 1.26 | -5.5 dB |
| Peaking | 116 Hz   | 3.28 | -7.0 dB |
| Peaking | 3652 Hz  | 4.24 | 8.0 dB  |
| Peaking | 8336 Hz  | 1.15 | -6.5 dB |
| Peaking | 18661 Hz | 1.85 | -7.1 dB |
| Peaking | 230 Hz   | 3.59 | 2.8 dB  |
| Peaking | 676 Hz   | 2.12 | 1.2 dB  |
| Peaking | 2268 Hz  | 4.4  | -2.2 dB |
| Peaking | 9096 Hz  | 6.59 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20770%2032%20Ohm/Beyerdynamic%20DT%20770%2032%20Ohm.png)