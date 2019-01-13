# Sony MDR-1000X Wired NC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -4.6; 23 -4.6; 25 -4.6; 28 -4.6; 31 -4.7; 34 -4.7; 37 -4.8; 41 -5.0; 45 -5.1; 49 -5.1; 54 -5.3; 60 -5.4; 66 -5.4; 72 -5.6; 79 -5.8; 87 -6.0; 96 -6.3; 106 -6.4; 116 -6.5; 128 -6.6; 141 -6.5; 155 -6.5; 170 -6.1; 187 -6.0; 206 -5.8; 227 -5.4; 249 -5.1; 274 -4.6; 302 -4.1; 332 -3.6; 365 -3.2; 402 -2.9; 442 -2.5; 486 -2.5; 535 -2.2; 588 -1.8; 647 -2.4; 712 -2.8; 783 -2.2; 861 -1.6; 947 -0.7; 1042 0.6; 1146 2.1; 1261 1.6; 1387 0.9; 1526 -1.2; 1678 -4.0; 1846 -6.2; 2031 -6.4; 2234 -4.9; 2457 -2.1; 2703 -1.7; 2973 -2.6; 3270 -2.8; 3597 -2.4; 3957 -5.1; 4353 -6.3; 4788 -3.9; 5267 -5.5; 5793 -7.4; 6373 -5.9; 7010 -2.9; 7711 -3.9; 8482 -5.3; 9330 -4.9; 10263 -2.9; 11289 -1.4; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wired NC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wired NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.23 | -4.1 dB |
| Peaking | 159 Hz   | 0.48 | -5.6 dB |
| Peaking | 1965 Hz  | 4.4  | -6.6 dB |
| Peaking | 5308 Hz  | 1.28 | -6.0 dB |
| Peaking | 9025 Hz  | 3.64 | -3.9 dB |
| Peaking | 759 Hz   | 2.66 | -1.8 dB |
| Peaking | 1219 Hz  | 2.6  | 3.5 dB  |
| Peaking | 1721 Hz  | 5.94 | -2.0 dB |
| Peaking | 3595 Hz  | 3.63 | -0.7 dB |
| Peaking | 13007 Hz | 3.06 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wired%20NC%20Active/Sony%20MDR-1000X%20Wired%20NC%20Active.png)