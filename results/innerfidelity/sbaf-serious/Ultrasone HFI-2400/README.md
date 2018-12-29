# Ultrasone HFI-2400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.0; 28 2.7; 31 1.5; 34 0.5; 37 -0.5; 41 -1.5; 45 -2.2; 49 -2.7; 54 -3.4; 60 -3.6; 66 -3.6; 72 -4.5; 79 -5.0; 87 -5.3; 96 -5.4; 106 -5.3; 116 -5.0; 128 -4.9; 141 -4.6; 155 -4.3; 170 -3.8; 187 -3.3; 206 -2.9; 227 -3.0; 249 -3.7; 274 -3.0; 302 -2.3; 332 -2.0; 365 -1.5; 402 -1.1; 442 -0.7; 486 -0.4; 535 0.0; 588 0.9; 647 0.5; 712 0.1; 783 0.3; 861 0.1; 947 -0.2; 1042 -0.2; 1146 -0.2; 1261 -0.2; 1387 -0.3; 1526 -0.6; 1678 -0.7; 1846 -1.1; 2031 0.2; 2234 4.6; 2457 6.0; 2703 3.7; 2973 1.8; 3270 -1.0; 3597 -2.2; 3957 -1.7; 4353 -1.5; 4788 3.2; 5267 4.2; 5793 -0.8; 6373 -9.3; 7010 -4.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.6; 13660 -5.0; 15026 -8.4; 16529 -7.8; 18182 -4.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-2400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.14 | 7.3 dB   |
| Peaking | 97 Hz    | 0.48 | -5.5 dB  |
| Peaking | 2471 Hz  | 4.96 | 7.0 dB   |
| Peaking | 3570 Hz  | 4.56 | -2.7 dB  |
| Peaking | 15867 Hz | 1.82 | -9.4 dB  |
| Peaking | 595 Hz   | 3.9  | 1.5 dB   |
| Peaking | 1800 Hz  | 5.4  | -1.9 dB  |
| Peaking | 5241 Hz  | 5.82 | 6.4 dB   |
| Peaking | 6454 Hz  | 5.75 | -11.3 dB |
| Peaking | 9023 Hz  | 1.27 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-2400/Ultrasone%20HFI-2400.png)